# -*- coding: utf-8 -*-
import logging
from stocktrader.utils.logger import log
from stocktrader.trader import ITrader
from stocktrader.trader_ths import TraderTHS
from stocktrader.trader_tdx import TraderTDX

traders = [TraderTHS, TraderTDX]

def register(*trader_class):
    """
    注册一个或者多个Itrader实现类
    :param trader_class: ITrader 实现类
    :return:
    """
    traders.extend([x for x in trader_class if issubclass(x, ITrader)])

def use(broker:str, debug=False, **kwargs):
    """
    根据券商类型选择合适的券商
    :param broker: 券商类型， ths/同花顺，tdx/通达信，zszq/招商证券
    :param debug: 控制日志输出Debug级别
    :param kwargs: 其他可选参数
    :return: ITrader 接口的实例类
    """
    if debug:
        log.setLevel(logging.DEBUG)

    for trader in traders:
        if broker.lower() in [x.strip() for x in trader.broker_types().split(",")]:
            return trader()
    log.warning("没有找到操作券商(%s)的客户端，使用默认同花顺客户端！", broker)
    return TraderTHS()

if __name__ == '__main__':
    # 使用示例，自定义的客户端类型可以使用register方法注册
    # register(TraderTDX)

    ths = use("ths", debug=True)
    ths.login("aimilin6688", "fgdaEzAFhPtDUMlu", broker="模拟炒股", nick_name="457138")
