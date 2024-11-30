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
    
    def __del__(self):
        lg.info(f"{self.usr} broker class destructor called")
        self.__logout()
    
    def __login(self):
        lg.info("Login done ...")
    
    def __logout(self):
        lg.info("Logout done ...")
    
    def __get_hist(self, ticker, interval, fromdate, todate, exchange):
        return ""
    
    def __place_order(self, ticker, quantity, buy_sell, exchange):
        return "ID1234"
    
    def __wait_till_order_fill(self, orderid):
        pass

    def __get_oder_status(self, orderid):
        return "complete"
    
    def __get_margin(self):
        return ""
    
    def __get_positions(self):
        return ""
    
    def __get_holdings(self):
        return ""
    
###############################################################################

    def get_user_data(self):
        return ""
    
    def get_margin(self):
        return 10000
    
    def get_current_price(self, ticker, exchange):
        return 100.00
    
    def hist_data_daily(self, ticker, duration, exchange):
        return ""
    
    def hist_data_intraday(self, ticker, exchange, datestamp=dt.date.today()):
        return ""
    
    def place_buy_order(self, ticker, quantity, exchange):
        buy_sell = "BUY"
        orderid = self.__place_order(ticker, quantity, buy_sell, exchange)
        self.__wait_till_order_fill(orderid)
        return orderid

    def place_sell_order(self, ticker, quantity, exchange):
            buy_sell = "SELL"
            orderid = self.__place_order(ticker, quantity, buy_sell, exchange)
            self.__wait_till_order_fill(orderid)
            return orderid
    
    def get_oder_status(self, orderid):
        status = self.__get_oder_status(orderid)
        return status
    
    def verify_position(self, sym, qty, exit=False):
        return True
    
    def verify_holding(self, sym, qty):
        return True
    
    def get_entry_exit_price(self, sym, _exit=False):
        if _exit:
            price = 150.00
        else:
            price = 100.00
        return price

