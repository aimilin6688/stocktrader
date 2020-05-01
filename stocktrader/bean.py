# -*- coding: utf-8 -*-

class Account:
    def __init__(self, username, password, broker=None, comm_password=None, nick_name=None, **kwargs):
        """
        账户信息
        :param username: 用户名
        :param password: 明文密码
        :param broker: 所属券商
        :param client: 客户端类型 字符串值需要与Client指定的值一样，或者直接使用定义的类型
        :param comm_password: 通讯密码
        :param nick_name: 多账户切换时需要设置昵称
        :param kwargs: 其他属性，可以通过.号直接访问
        """
        self.username = username
        self.password = password
        self.broker = broker
        self.comm_password = comm_password,
        self.nick_name = nick_name

        for k,v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return "%s(%s)"%(self.broker, self.nick_name or self.username)

class Result:
    """ 结果对象 """
    def __init__(self, state, data=None, **kwargs):
        self.state = state
        self.data = data
        for k,v in kwargs.items():
            setattr(self, k, v)

    @staticmethod
    def success(data=None, **kwargs):
        return Result("success", data, **kwargs)

    @staticmethod
    def fail(data=None, **kwargs):
        return Result("fail", data, **kwargs)

    def is_success(self):
        return self.state == "success"

    def is_fail(self):
        return self.state == "fail"


