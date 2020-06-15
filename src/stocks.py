#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:33:35 2020

@author: ehens86
"""

from db import populate

import argparse

valid_pos_args = ['DB']
valid_domains = ['SYMBOLS', 'INTRA', 'INTER']
#valid_models = ['LOG', 'LIGHT', 'DART']
#valid_dims = ['ML', 'ELO', 'BET']

def db_update(args):      
    if args.domain is None:
        raise('Domain required. Valid options: %s ' % [", ".join(valid_domains)])
    populate(args)
    
    
if __name__ == '__main__':
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Stock Scraping Engine')
    # Required positional argument
    parser.add_argument('pos_arg', type=str,
                        help='Function to trigger.  Valid options: %s' % [", ".join(valid_pos_args)])
    
    # Optional positional argument
    parser.add_argument('opt_pos_arg', type=int, nargs='?',
                        help='An optional integer positional argument')
    
    # Optional argument
    parser.add_argument('--domain', type=str,
                        help='Domain to activate.  Valid options: %s ' % [", ".join(valid_domains)])
    
    
    args = parser.parse_args()
    print("Argument values:")
    print(args.pos_arg)
    print(args.opt_pos_arg)
    print(args.domain)
    
    if args.pos_arg.upper()  not in valid_pos_args:
        raise ValueError("%s is not a valid command" % (args.pos_arg))
        
    if args.pos_arg.upper() == 'DB':
        db_update(args)
