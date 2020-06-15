#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:28:15 2020

@author: ehens86
"""

import requests
from datetime import datetime
from spring import addInstrument , getAllInstrumentSymbols, getInstrumentBySymbol, addPrice, getLatestPrice, getHistoricalRhDayPrices
from utils import progress
from joblib import Parallel, delayed

def add_stock(entry, _cur_stocks):
    if not entry['tradeable'] or entry['tradability'] != 'tradable':
        print('Not tradable')
        return
    
    if entry['type'] != 'stock':
        print('Not a stock')
        return
    
    if entry['symbol'] in _cur_stocks:
        print('Already included')
        return
    
    if entry['state'] != 'active':
        print(entry)
        raise
    
    rh_sym = entry['symbol']
    b_id = entry['bloomberg_unique']
    rh_id = entry['id']
    name = entry['name'].replace("'", '')
    country = entry['country']    
    daytrade_ratio = float(entry['day_trade_ratio'])
    listed = entry['list_date']
    
    payload = {'symbol': rh_sym,
               'bloombergId': b_id,
               'robinhoodId': rh_id,
               'name': name,
               'country': country,
               'dayTradeRatio': daytrade_ratio,
               'listedDate': listed
               }
    resp = addInstrument(payload)
    if resp['errorMsg'] is not None:
        print(resp['errorMsg'])
        
def loop_rh_stock_get(data_dict, _cur_stocks):
    for entry in data_dict['results']:
        add_stock(entry, _cur_stocks)
        
def _pop_stocks():
    url = 'https://api.robinhood.com/instruments/'
    data_dict = requests.get(url).json()
    _cur_stocks = getAllInstrumentSymbols()
    loop_rh_stock_get(data_dict, _cur_stocks)
    while True:
        url = data_dict['next']
        data_dict = requests.get(url).json()
        loop_rh_stock_get(data_dict, _cur_stocks)
        if data_dict['next'] is None:
            break   
        
def _pop_each_inter_price(inst_oid, hist, latest_ts, debug = True):
    price_ts = datetime.strptime(hist['begins_at'].replace('Z',''), '%Y-%m-%dT%H:%M:%S')
    if latest_ts is not None and price_ts <= latest_ts:
        return
    add_price_payload = {}
    add_price_payload['timestamp'] = hist['begins_at']
    add_price_payload['openPrice'] = hist['open_price']
    add_price_payload['closePrice'] = hist['close_price']
    add_price_payload['highPrice'] = hist['high_price']
    add_price_payload['lowPrice'] = hist['low_price']
    add_price_payload['volume'] = hist['volume']
    add_price_payload['type'] = 'INTRA_DAY'
    resp = addPrice(inst_oid, add_price_payload)
    if resp['errorMsg'] is not None and debug:
        print(resp['errorMsg'])
    
def _pop_instrument_inter_price(sym):
#    sym = 'APDN'
    latest_ts = None
    inst = getInstrumentBySymbol(sym)
    latest_price = getLatestPrice(inst['oid'], 'INTRA_DAY')
    if len(latest_price) != 0:
        latest_ts = datetime.strptime(latest_price[0], '%Y-%m-%d %H:%M:%S.%f')
    data = getHistoricalRhDayPrices(sym, debug = True)
    for hist in data:
        _pop_each_inter_price(inst['oid'], hist, latest_ts)   
       
def _pop_inter_prices():
    all_symbols = getAllInstrumentSymbols()
    Parallel(n_jobs = 4, verbose = 10)(delayed(_pop_instrument_inter_price) (i) for i in all_symbols)

            
def populate(args):
    if args.domain.upper() == 'SYMBOLS':
        _pop_stocks()
    elif args.domain.upper() == 'INTER':
        _pop_inter_prices()

    
