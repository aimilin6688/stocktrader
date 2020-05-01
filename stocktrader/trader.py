# -*- coding: utf-8 -*-
import abc
from stocktrader.bean import Account, Result

class ITrader(abc.ABC):
    """
    交易接口：
    注意：交易客户端需要打开 “委托成功是否弹出对话框”：是，否则委托不能获取到委托编号
    """
    @staticmethod
    @abc.abstractmethod
    def broker_types() -> str:
        """
        客户端支持的券商类型, 多个以英文逗号分隔
        :return:同花顺,大通证券
        """
        pass

    @abc.abstractmethod
    def login(self, username=None, password=None, broker=None, comm_password=None, nick_name=None,account:Account=None, **kwargs) -> Result:
        """
        客户端登录
        :param account: 账户密码等信息,设置该参数可以不用设置其他参数
        :param username: 用户名（必填）
        :param password: 密码（必填）
        :param broker: 券商(可选)
        :param comm_password: 通信密码(可选)
        :param nick_name: 昵称，多账户切换必填，否则可选
        :param kwargs: 直接添加到结果对象中
        :return:成功：{"state":"success"},失败：{"state":"fail", "data":失败原因或异常}
        """
        pass

    @abc.abstractmethod
    def buy(self, code, price, amount, **kwargs) -> Result:
        """
        买入股票
        :param code: 股票代码, 支持sh600365, 600365, 600365.SH
        :param price: 委托价格
        :param amount: 委托数量
        :param kwargs: 直接添加到结果对象中
        :return:成功：{"state":"success", "data":委托详细, "entrust_no":委托单号}，
        失败：{"state":"fail", "data":"异常信息或所有弹框信息"}
        """
        pass

    @abc.abstractmethod
    def sell(self, code, price, amount, **kwargs) -> Result:
        """
        卖出股票
        :param code: 股票代码, 支持sh600365, 600365, 600365.SH
        :param price: 委托价格
        :param amount: 委托数量
        :param kwargs: 直接添加到结果对象中
        :return:成功：{"state":"success", "data":委托详细，"entrust_no":委托单号}，
        失败：{"state":"fail", "data":"异常信息或所有弹框信息"}
        """
        pass

    @abc.abstractmethod
    def market_buy(self,code, amount, entrust_type=None, limit_price=None, **kwargs) -> Result:
        """
        市价买入
        :param code: 股票代码, 支持sh600365, 600365, 600365.SH
        :param amount: 委托数量
        :param entrust_type: 市价委托类型，默认客户端默认选择，
                     深市可选 ['对手方最优价格', '本方最优价格', '即时成交剩余撤销', '最优五档即时成交剩余 '全额成交或撤销']
                     沪市可选 ['最优五档成交剩余撤销', '最优五档成交剩余转限价']
        :param limit_price: 科创板限价
        :param kwargs: 直接添加到结果对象中
        :return:成功：{"state":"success", "data":委托详细，"entrust_no":委托单号}，
        失败：{"state":"fail", "data":"异常信息或所有弹框信息"}
        """

    @abc.abstractmethod
    def market_sell(self,code, amount, entrust_type=None, limit_price=None, **kwargs) -> Result:
        """
        市价卖出
        :param code:股票代码, 支持sh600365, 600365, 600365.SH
        :param amount: 委托数量
        :param entrust_type: 市价委托类型，默认客户端默认选择，
                     深市可选 ['对手方最优价格', '本方最优价格', '即时成交剩余撤销', '最优五档即时成交剩余 '全额成交或撤销']
                     沪市可选 ['最优五档成交剩余撤销', '最优五档成交剩余转限价']
        :param limit_price: 科创板限价
        :param kwargs: 直接添加到结果对象中
        :return:成功：{"state":"success", "data":委托详细，"entrust_no":委托单号}，
        失败：{"state":"fail", "data":"异常信息或所有弹框信息"}
        """
        pass

    @abc.abstractmethod
    def money(self, **kwargs) -> Result:
        """
        资金情况
        :param kwargs: 直接添加到结果对象中
        :return:成功：{"state":"success", "data":{资金信息}}，
        失败：{"state":"fail", "data":"失败原因或者异常信息"}
        """
        pass

    @abc.abstractmethod
    def position(self, **kwargs) -> Result:
        """
        当前持仓
        :param kwargs:直接添加到结果对象中
        :return:成功：{"state":"success", "data":[数据列表]}，
        失败：{"state":"fail", "data":"失败原因或者异常信息"}
        """
        pass

    @abc.abstractmethod
    def entrust(self, **kwargs) -> Result:
        """
        今日委托
        :param kwargs:直接添加到结果对象中
        :return:成功：{"state":"success", "data":[数据列表]}，
        失败：{"state":"fail", "data":"失败原因或者异常信息"}
        """
        pass

    @abc.abstractmethod
    def trade(self, **kwargs) -> Result:
        """
        今日成交
        :param kwargs:直接添加到结果对象中
        :return:成功：{"state":"success", "data":[数据列表]}，
        失败：{"state":"fail", "data":"失败原因或者异常信息"}
        """
        pass

    @abc.abstractmethod
    def cancel_entrust(self, entrust_nos, **kwargs) -> Result:
        """
        撤销委托
        :param kwargs:直接添加到结果对象中
        :param entrust_nos: 多个委托逗号分隔，或者['00002','00003']
        :return:成功：{"state":"success", "data":{'00002':{'state':"success", "data":"失败原因(失败会有)"}}}
        """
        pass

class BaseTrader(ITrader):
    """
    同花顺或者大通证券公共方法抽取
    """
    pass



