# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:36:02 2024

@author: ashwe
"""

from logger import *

class stub:
    def __init__(self, usr_="NO_USR"):
        self.usr = usr_
        self.cp = 100.00
        lg.info(f"{self.usr} stub broker class constructor called")
        self.__i = 0

    def __del__(self):
        lg.info(f"{self.usr} stub broker class destructor called")

    def __login(self):
        lg.done(f"{self.usr} stub broker class Login done ...")

    def __logout(self):
        lg.done(f"{self.usr} stub broker class Logout done ...")

    def __place_order(self, ticker, quantity, buy_sell, exchange):
        orderid = "ANGEL_ID1234"
        lg.info(f"{self.usr} stub broker class placing order")
        lg.info("{} orderid: {} for {}".format(buy_sell, orderid, ticker))
        return orderid

    def __read_dummy_ltp(self):
        try:
            with open("../ltp.txt") as file:
                data = file.readlines()
                if self.__i > len(data) - 1:
                    self.__i = 0
                ltp = float(data[self.__i])
                self.__i = self.__i + 1
        except Exception as err: 
            print(err)
            ltp = float(input("Enter current price:\n"))
        return ltp

    def get_user_data(self):
        lg.info(f"{self.usr} stub broker getting user data")
        return ""

    def get_trade_margin(self):
        lg.info(f"{self.usr} stub broker getting trade margin")
        return 10000

    def get_current_price(self, ticker, exchange):
        lg.info(f"{self.usr} stub broker current price")
        self.cp = self.__read_dummy_ltp()
        return self.cp

    def hist_data_daily(self, ticker, duration, exchange):
        lg.info(f"{self.usr} stub broker hist_data_daily")
        return ""

    def hist_data_intraday(self, ticker, exchange, datestamp=dt.date.today()):
        lg.info(f"{self.usr} stub broker hist_data_intraday")
        return ""

    def place_buy_order(self, ticker, quantity, exchange):
        lg.info(f"{self.usr} stub broker place_buy_order")

    def place_sell_order(self, ticker, quantity, exchange):
        lg.info(f"{self.usr} stub broker place_sell_order")

    def get_oder_status(self, orderid):
        lg.info(f"{self.usr} stub broker class getting order status")
        return "complete"

    def verify_position(self, sym, qty, exit=False):
        lg.info(f"{self.usr} stub broker verify_position")

    def verify_holding(self, sym, qty):
        lg.info(f"{self.usr} stub broker verify_holding")

    def get_entry_exit_price(self, sym, _exit=False):
        lg.info(f"{self.usr} stub broker get_entry_exit_price")
        if _exit:
            price = self.cp
        else:
            price = self.cp
        return price
