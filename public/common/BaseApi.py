# !/usr/bin/python
# -*- encoding = utf-8 -*-
# author: liuwei


from airtest.core.api import *
from poco.drivers.ios import iosPoco
from public.common.createlog import Runlogger


class BaseMethod(object):

    def __init__(self):
        self.poco = iosPoco()
        self.runLog = Runlogger().debug_log()

    def findElement(self):
        pass

    def p_click(self, pos):
        '''
        单击方法
        '''
        try:
            self.poco.click(pos)
        except Exception as e:
            self.runLog.error(f'单击方法失效{e}')
            raise e

    def p_long_click(self, pos):
        '''
        长按方法
        :return:
        '''
        try:
            self.poco.long_click(pos)
        except Exception as e:
            self.runLog.error(f'长按方法失效{e}')
            raise e

    def p_swipe(self, p1, p2):
        '''
        按坐标滑动方法，屏幕开始位置为【0，0】【1，1】
        :return:
        '''
        try:
            self.poco.swipe(p1, p2, direction=None, duration=2.0)
        except Exception as e:
            self.runLog.error(f'滑动方法失效:{e}')
            raise e

    def p_pinch(self, direction):
        '''
        按坐标滑动方法，屏幕开始位置为【0，0】【1，1】
        :return:
        '''
        try:
            if direction == "u'in'":
                self.poco.pinch(direction=u'in', percent=0.6, duration=2.0, dead_zone=0.1)
            elif direction == "u'out'":
                self.poco.pinch(direction=u'out', percent=0.6, duration=2.0, dead_zone=0.1)
            else:
                self.runLog.error('pinch 方法 参数错误')
        except Exception as e:
            self.runLog.error(f'扩展挤压方法失效:{e}')
            raise e

    def a_touch(self, *args, **kwargs):
        '''
        根据图片点击的方法
        :return:
        '''
        try:
            touch(*args, **kwargs)
        except Exception as e:
            self.runLog.error(f'滑动方法失效:{e}')
            raise e

    def a_wait(self):
        '''
        根据图片点击的方法
        :return:
        '''
        try:
            wait()
        except Exception as e:
            self.runLog.error(f'滑动方法失效:{e}')
            raise e

    def a_swipe(self, fpos, tpos, duration=0.5, steps=5, fingers=1):
        '''
        根据图片等待的方法
        :return:
        '''
        try:
            swipe(fpos, tpos, duration=0.5, steps=5, fingers=1)
        except Exception as e:
            self.runLog.error(f'等待方法失效:{e}')
            raise e

    def a_text(self, *args, **kwargs):
        '''
        输入的方法
        :return:
        '''
        try:
            text(*args, **kwargs)
        except Exception as e:
            self.runLog.error(f'输入方法失效:{e}')
            raise e
