# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:07:10 2024

@author: ashwe
"""

from logger import *

class broker:
    def __init__(self, usr_="NO_USR"):
        self.usr = usr_
        lg.info(f"{self.usr} broker class constructor called")        
        self._instance = None
        self.__login()
        self.cp = 100.00
    
    def __del__(self):
        lg.info(f"{self.usr} broker class destructor called")
        self.__logout()
    
    def __login(self):
        lg.info("Login done ...")
    
    def __logout(self):
        lg.info("Logout done ...")
    
    def __place_order(self, ticker, quantity, buy_sell, exchange):
        return "ID1234"
    
    def __wait_till_order_fill(self, orderid):
        count = 0
        lg.info('Buy order is in open, waiting ... %d ' % count)
        while self.__get_oder_status(orderid) == 'open':
            lg.info('Buy order is in open, waiting ... %d ' % count)
            count = count + 1

    def __get_oder_status(self, orderid):
        return "complete"
    
###############################################################################

    def get_user_data(self):
        return ""
    
    def get_trade_margin(self):
        return 10000
    
    def get_current_price(self, ticker, exchange):
        self.cp = float(input("Enter current price:\n"))
        return self.cp
    
    def hist_data_daily(self, ticker, duration, exchange):
        return ""
    
    def hist_data_intraday(self, ticker, exchange, datestamp=dt.date.today()):
        return ""
    
    def place_buy_order(self, ticker, quantity, exchange):
        buy_sell = "BUY"
        orderid = self.__place_order(ticker, quantity, buy_sell, exchange)
        self.__wait_till_order_fill(orderid)
        status = self.__get_oder_status(orderid)
        if status == 'complete':
            return True
        else:
            return False

    def place_sell_order(self, ticker, quantity, exchange):
            buy_sell = "SELL"
            orderid = self.__place_order(ticker, quantity, buy_sell, exchange)
            self.__wait_till_order_fill(orderid)
            status = self.__get_oder_status(orderid)
            if status == 'complete':
                return True
            else:
                return False
    
    def verify_position(self, sym, qty, exit=False):
        return True
    
    def verify_holding(self, sym, qty):
        return True
    
    def get_entry_exit_price(self, sym, _exit=False):
        if _exit:
            price = self.cp
        else:
            price = self.cp
        return price

