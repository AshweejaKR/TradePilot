# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:11:42 2024

@author: ashwe
"""

from logger import *
from autotick import *

def main():

    initialize_logger()
    # lg.info("main running ...")

    ticker = "INFY"
    exchange = "NSE"
    obj = autotick(ticker, exchange)
    obj.run_strategy()
    
if __name__ == "__main__":
    main()
