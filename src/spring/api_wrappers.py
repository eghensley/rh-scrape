#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:22:50 2020

@author: ehens86
"""

if (__name__ == "__main__"):
    import sys
    sys.path.append("..")

from spring.config import CONFIG

import requests 

def getInstrumentBySymbol(symbol, debug = False):
    while True:
        try:
            r = requests.get(url = CONFIG['spring']['rest']['GET_INSTRUMENT_BY_SYMBOL'] % (CONFIG['spring']['HOST'], CONFIG['spring']['PORT'], symbol))
            response = r.json() 
            if response['errorMsg'] is not None and debug:
                print(response['errorMsg'])
            return response['response']
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            pass
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            pass
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            pass
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)  
            pass
        
def getInstrumentByRhId(rh_id, debug = False):
    while True:
        try:
            r = requests.get(url = CONFIG['spring']['rest']['GET_INSTRUMENT_BY_RH_ID'] % (CONFIG['spring']['HOST'], CONFIG['spring']['PORT'], rh_id))
            response = r.json() 
            if response['errorMsg'] is not None and debug:
                print(response['errorMsg'])
            return response['response']
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            pass
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            pass
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            pass
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)  
            pass
        
def getAllInstrumentSymbols(debug = False):
    while True:
        try:
            r = requests.get(url = CONFIG['spring']['rest']['GET_ALL_SYMBOLS'] % (CONFIG['spring']['HOST'], CONFIG['spring']['PORT']))
            response = r.json() 
            if response['errorMsg'] is not None and debug:
                print(response['errorMsg'])
            return response['response']
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            pass
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            pass
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            pass
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)  
            pass
        
def addInstrument(payload):
    while True:
        try:
            r = requests.post(url = CONFIG['spring']['rest']['ADD_NEW_INSTRUMENT'] % (CONFIG['spring']['HOST'], CONFIG['spring']['PORT']), json = payload)
            response = r.json()
            return response
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            pass
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            pass
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            pass
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)  
            pass
        
def addPrice(instrument_oid, payload):
    while True:
        try:
            r = requests.post(url = CONFIG['spring']['rest']['ADD_NEW_PRICE'] % (CONFIG['spring']['HOST'], CONFIG['spring']['PORT'], instrument_oid), json = payload)
            response = r.json()
            return response
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            pass
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            pass
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            pass
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)  
            pass
        
def getLatestPrice(instrument_oid, price_type, debug = False):
    while True:
        try:
            r = requests.get(url = CONFIG['spring']['rest']['GET_LATEST_PRICE'] % (CONFIG['spring']['HOST'], CONFIG['spring']['PORT'], instrument_oid, price_type))
            response = r.json() 
            if response['errorMsg'] is not None and debug:
                print(response['errorMsg'])
            return response['response']
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            pass
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            pass
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            pass
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)  
            pass
        
def getHistoricalRhDayPrices(symbol, debug = False):
    while True:
        try:
            r = requests.get(url = CONFIG['flask']['rest']['GET_DAY_PRICES'] % (CONFIG['flask']['HOST'], CONFIG['flask']['PORT'], CONFIG['flask']['CONTEXT'], symbol))
            response = r.json() 
            if response['errorMsg'] is not None and debug:
                print(response['errorMsg'])
            return response['payload']
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            pass
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            pass
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            pass
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)  
            pass