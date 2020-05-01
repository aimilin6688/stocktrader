# -*- coding: utf-8 -*-
from stocktrader.utils.logger import log
from pywinauto.findwindows import find_windows
from pywinauto.controls.hwndwrapper import DialogWrapper


# 弹框处理工具类
class PopupHelper(object):

    @staticmethod
    def close_team_viewer():
        # 关闭TeamViewer新特性弹出框
        try:
            ds = find_windows(class_name="#32770", title="TeamViewer", visible_only=True)
            for x in ds:
                DialogWrapper(x).close()
                log.debug("关闭TeamViewer弹出框：%x", x)
        except:
            pass


if __name__ == '__main__':
    PopupHelper.close_team_viewer()