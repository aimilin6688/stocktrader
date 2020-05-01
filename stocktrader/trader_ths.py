# -*- coding: utf-8 -*-

from bean import Result, Account
from stocktrader.utils.constant import Constant
from stocktrader.utils.logger import log
from stocktrader.trader import BaseTrader

class TraderTHS(BaseTrader):
    """
    同花顺客户端操作
    """
    @staticmethod
    def broker_types() -> str:
        return "ths,同花顺"

    def login(self, username=None, password=None, broker=None, comm_password=None, nick_name=None,account:Account=None,  **kwargs) -> Result:
        from stocktrader.utils.login_helper import LoginTHS
        return LoginTHS(self).login(username=username, password=password,broker=broker,comm_password=comm_password, nick_name=nick_name, account=account, **kwargs)

    def buy(self, code, price, amount, **kwargs) -> Result:
        pass

    def sell(self, code, price, amount, **kwargs) -> Result:
        pass

    def market_buy(self, code, amount, entrust_type=None, limit_price=None, **kwargs) -> Result:
        pass

    def market_sell(self, code, amount, entrust_type=None, limit_price=None, **kwargs) -> Result:
        pass

    def money(self, **kwargs) -> Result:
        pass

    def position(self, **kwargs) -> Result:
        pass

    def entrust(self, **kwargs) -> Result:
        pass

    def trade(self, **kwargs) -> Result:
        pass

    def cancel_entrust(self, entrust_nos, **kwargs) -> Result:
        pass