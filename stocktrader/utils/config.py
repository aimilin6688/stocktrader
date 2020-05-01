# -*- coding:utf-8 -*-
import configparser
import os

root_path = os.path.dirname(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))
class Config:
    def __init__(self, config_path=None, encoding="UTF-8"):
        if not config_path:
            config_path = os.path.join(root_path, "config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(config_path, encoding=encoding)
        self.root_path = root_path

    @property
    def log_path(self):
        return self.get("log", "log_path")


    def get(self,section, option, default_value=""):
        return self.config.get(section, option, fallback=default_value)

config = Config()

if __name__ == '__main__':
    print(Config().get("log", 'log_path'))