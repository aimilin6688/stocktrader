# -*- coding:utf-8 -*-
import os
import logging
from logging import handlers
from stocktrader.utils.config import config

def _mk_path(path:str=None):
    if not path:
        path = os.path.join(config.root_path, 'data', 'logs', 'stock-trader.log')
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    return path

log = logging.getLogger("stock-trader")
log.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(asctime)s %(levelname)s [%(filename)s %(funcName)s:%(lineno)d]-%(thread)d: %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(fmt)
log.addHandler(console_handler)

file_handler = handlers.TimedRotatingFileHandler(_mk_path(config.log_path), when="D", backupCount=30, encoding="utf-8")
file_handler.setFormatter(fmt)
log.addHandler(file_handler)

if __name__ == '__main__':
    log.info("test")