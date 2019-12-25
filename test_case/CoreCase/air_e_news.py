# !/usr/bin/python
# -*- encoding = utf-8 -*-
# author: liuwei

import unittest
from airtest.core.api import *
from public.common.BaseApi import BaseMethod
from airtest.cli.parser import cli_setup
from config import globelsetting
from public.common.decorator import recase


class RegisterAndLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logdir = globelsetting.alog_path
        if not cli_setup():
            auto_setup(__file__, logdir=cls.logdir, devices=[
                "ios:///http://127.0.0.1:8100",
            ])
        # 连接设备
        # connect_device('http://169.254.99.81:8100')

    def setUp(self):
        # 通过包名打开app
        start_app('xiaozhu.com.XZTenant')
        sleep(2)
        # 创建基础方法对象
        self.driver = BaseMethod()
        self.pic_path = globelsetting.CorePic_path

    def tearDown(self):
        home()

    @recase(setUp, tearDown, 4)
    def test_sendnews(self):
        '''
        房客发送消息
        '''
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/news/newsTab.png",
                                     record_pos=(0.128, 0.964), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/news/chatobject.png",
                                     record_pos=(-0.216, -0.279), resolution=(1125, 2436)))
        sleep(1)
        self.driver.p_click([0.404, 0.9291871921182266])
        self.driver.a_text("小猪猪")
        assert_not_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/news/assertnews.png",
                                   record_pos=(0.109, -0.148), resolution=(1125, 2436)), "发送成功")


if __name__ == "__main__":
    unittest.main()
