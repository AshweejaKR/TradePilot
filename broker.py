# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:07:10 2024

@author: ashwe
"""

from logger import *
from angleone_broker import *
from aliceblue_broker import *

class broker:
    def __init__(self, usr_="NO_USR"):
        self.usr = usr_
        lg.info(f"{self.usr} broker class constructor called")
        self._instance = None
        # self._instance = angleone()
        # self._instance = aliceblue()
    
    def __del__(self):
        lg.info(f"{self.usr} broker class destructor called")

    def __wait_till_order_fill(self, orderid, order):
        count = 0
        lg.info('%s order is in open, waiting ... %d ' % (order, count))
        while self._instance.get_oder_status(orderid) == 'open':
            lg.info('%s order is in open, waiting ... %d ' % (order, count))
            count = count + 1

###############################################################################

    def get_user_data(self):
        usr = self._instance.get_user_data()
        return usr
    
    def get_trade_margin(self):
        margin = self._instance.get_trade_margin()
        return margin
    
    def get_current_price(self, ticker, exchange):
        cp = self._instance.get_current_price(ticker, exchange)
        return cp

    def hist_data_daily(self, ticker, duration, exchange):
        self._instance.hist_data_daily(ticker, duration, exchange)
    
    def hist_data_intraday(self, ticker, exchange, datestamp=dt.date.today()):
        self._instance.hist_data_intraday(ticker, exchange, datestamp=dt.date.today())
    
    def place_buy_order(self, ticker, quantity, exchange):
        buy_sell = "BUY"
        orderid = self._instance.place_buy_order(ticker, quantity, exchange)
        self.__wait_till_order_fill(orderid, buy_sell)
        status = self._instance.get_oder_status(orderid)
        if status == 'complete':
            return True
        else:
            return False

    def place_sell_order(self, ticker, quantity, exchange):
        buy_sell = "SELL"
        orderid = self._instance.place_sell_order(ticker, quantity, exchange)
        self.__wait_till_order_fill(orderid, buy_sell)
        status = self._instance.get_oder_status(orderid)
        if status == 'complete':
            return True
        else:
            return False
    
    def verify_position(self, sym, qty, exit=False):
        return True
    
    def verify_holding(self, sym, qty):
        return True
    
    def get_entry_exit_price(self, sym, _exit=False):
        ep = self._instance.get_entry_exit_price(sym, _exit)
        return ep
