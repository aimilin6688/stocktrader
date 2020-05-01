# -*- coding: utf-8 -*-
import abc
from stocktrader.bean import Account,Result
from stocktrader.utils.logger import log

class BaseLogin(abc.ABC):

    def __init__(self, trader):
        self.trader = trader

    def login(self, username=None, password=None, broker=None, comm_password=None, nick_name=None,account:Account=None, **kwargs) -> Result:
        account = account or Account(username, password, broker=broker, comm_password=comm_password,nick_name=nick_name, **kwargs)
        return self._login(account)

    def _login(self, account:Account):
        log.debug("准备登录账户：%s", account)
        self.trader.account = account
        return self._change_account(account) if self._is_login(account) else self._login_account(account)

    @abc.abstractmethod
    def _change_account(self, account) -> Result:
        """
        切换账号信息
        :param account:
        :return: 成功：{"state":"success"},失败：{"state":"fail", "data":失败原因或异常}
        """
        pass

    @abc.abstractmethod
    def _is_login(self, account) -> bool:
        """
        判断账户是否登录成功
        :param account:
        :return: True 登录成功，False 登录失败
        """
        pass

    @abc.abstractmethod
    def _login_account(self, account) -> Result:
        """
        登录指定账户
        :param account:
        :return: 成功：{"state":"success"},失败：{"state":"fail", "data":失败原因或异常}
        """
        pass


class LoginTHS(BaseLogin):
    """
    同花顺登录
    """
    def _change_account(self, account) -> Result:
        pass

    def _is_login(self, account) -> bool:
        pass

    def _login_account(self, account) -> Result:
        pass


class LoginTDX(BaseLogin):
    """
    通达信登录
    """
    def _change_account(self, account) -> Result:
        pass

    def _is_login(self, account) -> bool:
        pass

    def _login_account(self, account) -> Result:
        pass