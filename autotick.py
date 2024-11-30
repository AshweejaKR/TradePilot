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
        self.stoploss_price = self.entry_price - (self.entry_price * 0.1)

    def __set_takeprofit(self):
        self.takeprofit_price = self.entry_price + (self.entry_price * 0.2)

    def __get_cur_price(self):
        cp = self.obj.get_current_price(self.ticker, self.exchange)
        return cp

    def __load_positions(self):
        data = load_positions(self.ticker)
        if data is not None:
            try:
                if self.ticker == data['ticker']:
                    self.quantity = data['quantity']
                    res = self.obj.verify_holding(self.ticker, self.quantity)

                    if res:
                        self.current_trade = data['order_type']
                        self.entry_price = data['entryprice']
                        self.stoploss_price = data['stoploss']
                        self.takeprofit_price = data['takeprofit']

            except Exception as err:
                template = "An exception of type {0} occurred. error message:{1!r}"
                message = template.format(type(err).__name__, err.args)
                lg.error("ERROR: {}".format(message))
                send_to_telegram(message)

    def init_strategy(self):
        pass
    
    def run_strategy(self):
        self.init_strategy()
        wait_till_market_open()
        self.__load_positions()
        while is_market_open():
            try:
                lg.info("Running Trade For {} ... ".format(self.ticker))
                self.__load_positions()
                ret = self.strategy()
                cur_price = self.__get_cur_price()

                if self.current_trade == "BUY":
                    lg.info('SL %.2f <-- %.2f --> %.2f TP' % (self.stoploss_price, cur_price, self.takeprofit_price))

                if self.current_trade == "NA" and (ret == "BUY"):
                    lg.info("Entering Trade")
                    amt = self.obj.get_margin()
                    lg.info("cash available: {} ".format(amt))
                    amt_for_trade = min(amt, self.capital_per_trade)
                    lg.info("cash using for trade: {} ".format(amt_for_trade))
                    self.quantity = int(amt_for_trade / cur_price)
                    lg.info("quantity: {} ".format(self.quantity))
                    orderid = self.obj.place_buy_order(self.ticker, self.quantity, self.exchange)
                    lg.info("orderid: {} ".format(orderid))
                    status = self.obj.get_oder_status(orderid)
                    lg.info("status: {} ".format(status))
                    if status == 'complete':
                        res = self.obj.verify_position(self.ticker, self.quantity)
                        self.entry_price = self.obj.get_entry_exit_price(self.ticker)
                        self.__set_stoploss()
                        self.__set_takeprofit()
                        self.current_trade = "BUY"
                        save_positions(self.ticker, self.quantity, self.current_trade, self.entry_price, self.stoploss_price, self.takeprofit_price)
                        save_trade_in_csv(self.ticker, self.quantity, "BUY", self.entry_price)
                        lg.info('Submitted {} Order for {}, Qty = {} at price: {}'.format("BUY",
                                                                                               self.ticker,
                                                                                               self.quantity,
                                                                                               self.entry_price))
                
                elif (self.current_trade == "BUY") and (ret == "SELL"):
                    lg.info("Exiting Trade")
                    orderid = self.obj.place_sell_order(self.ticker, self.quantity, self.exchange)
                    lg.info("orderid: {} ".format(orderid))
                    status = self.obj.get_oder_status(orderid)
                    lg.info("status: {} ".format(status))
                    if status == 'complete':
                        res = self.obj.verify_position(self.ticker, self.quantity)
                        exit_price = self.obj.get_entry_exit_price(self.ticker, True)
                        self.current_trade = "NA"
                        remove_positions(self.ticker)
                        save_trade_in_csv(self.ticker, self.quantity, "SELL", exit_price)
                        lg.info('Submitted {} Order for {}, Qty = {} at price: {}'.format("SELL",
                                                                                               self.ticker,
                                                                                               self.quantity,
                                                                                               exit_price))
                
                elif (self.current_trade == "BUY") and (cur_price > self.takeprofit_price):
                    lg.info("Exiting Trade")
                    orderid = self.obj.place_sell_order(self.ticker, self.quantity, self.exchange)
                    lg.info("orderid: {} ".format(orderid))
                    status = self.obj.get_oder_status(orderid)
                    lg.info("status: {} ".format(status))
                    if status == 'complete':
                        res = self.obj.verify_position(self.ticker, self.quantity)
                        exit_price = self.obj.get_entry_exit_price(self.ticker, True)
                        self.current_trade = "NA"
                        remove_positions(self.ticker)
                        save_trade_in_csv(self.ticker, self.quantity, "SELL", exit_price)
                        lg.info('Submitted {} Order for {}, Qty = {} at price: {}'.format("SELL",
                                                                                               self.ticker,
                                                                                               self.quantity,
                                                                                               exit_price))

                elif (self.current_trade == "BUY") and (cur_price < self.stoploss_price):
                    lg.info("Exiting Trade")
                    orderid = self.obj.place_sell_order(self.ticker, self.quantity, self.exchange)
                    lg.info("orderid: {} ".format(orderid))
                    status = self.obj.get_oder_status(orderid)
                    lg.info("status: {} ".format(status))
                    if status == 'complete':
                        res = self.obj.verify_position(self.ticker, self.quantity)
                        exit_price = self.obj.get_entry_exit_price(self.ticker, True)
                        self.current_trade = "NA"
                        remove_positions(self.ticker)
                        save_trade_in_csv(self.ticker, self.quantity, "SELL", exit_price)
                        lg.info('Submitted {} Order for {}, Qty = {} at price: {}'.format("SELL",
                                                                                               self.ticker,
                                                                                               self.quantity,
                                                                                               exit_price))

                
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
