# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:21:09 2024

@author: ashwe
"""

import time

from broker import *
from utils import *

class autotick:
    def __init__(self, ticker, exchange):
        lg.info("autotick class constructor called")
        self.name = "autotick"
        self.current_trade = "NA"
        self.ticker = ticker
        self.interval = 1
        self.exchange = exchange
        self.obj = broker(self.ticker)
        self.quantity = None
        self.entry_price = None
        self.takeprofit_price = None
        self.stoploss_price = None
        self.capital_per_trade = 1000.00

    def __del__(self):
        lg.info("autotick class destructor called")

    def __set_stoploss(self):
        self.stoploss_price = self.entry_price - (self.entry_price * 0.01)

    def __set_takeprofit(self):
        self.takeprofit_price = self.entry_price + (self.entry_price * 0.02)

    def __get_cur_price(self):
        cp = self.obj.get_current_price(self.ticker, self.exchange)
        return cp

    def __load_positions(self):
        pass
    
    def init_strategy(self):
        pass
    
    def run_strategy(self):
        self.init_strategy()
        wait_till_market_open()
        
        while is_market_open():
            try:
                lg.info("Running Trade For {} ... ".format(self.ticker))
                self.__load_positions()
                ret = self.strategy()
                
                if self.current_trade == "NA" and (ret == "BUY"):
                    lg.info("Entering Trade")
                    self.current_trade = "BUY"
                
                elif (self.current_trade == "BUY") and (ret == "SELL"):
                    lg.info("Exiting Trade")
                    self.current_trade = "NA"
                
                elif (self.current_trade == "BUY") and (cur_price > self.takeprofit_price):
                    lg.info("Exiting Trade")
                    self.current_trade = "NA"

                elif (self.current_trade == "BUY") and (cur_price < self.stoploss_price):
                    lg.info("Exiting Trade")
                    self.current_trade = "NA"

                
                time.sleep(self.interval)

            except KeyboardInterrupt:
                lg.error("Bot stop request by user")
                break

            except Exception as err:
                template = "An exception of type {0} occurred. error message:{1!r}"
                message = template.format(type(err).__name__, err.args)
                lg.error("{}".format(message))
                break

########################### dummy strategy ####################################
    def strategy(self):
        x = int(input("Enter Trend:\n"))
        if x == 1:
            return "BUY"
        
        elif x == 2:
            return "SELL"
        
        else:
            return "NA"
###############################################################################
