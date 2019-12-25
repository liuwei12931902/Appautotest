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

    # @recase(setUp, tearDown, 4)
    def test_login(self):
        '''
        1.进入房客中心，点击登录按钮,进入短信快捷登录页面
        '''
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/login/mobilelogin.png",
                                     record_pos=(-0.113, 0.789), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/login/step_mobile.png",
                                     record_pos=(-0.147, -0.267), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_text('15510136069')
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/login/step_getCode.png",
                                     record_pos=(0.29, -0.067), resolution=(1125, 2436)))

        if exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/login/yichangassert.png",
                           record_pos=(0.001, 0.0), resolution=(1125, 2436))):
            self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/login/yichanglongin.png",
                           record_pos=(-0.012, 0.132), resolution=(1125, 2436)))
            self.driver.p_click( [0.676, 0.9384236453201971])
            sleep(3)
        else:
            sleep(5)
            self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/login/step_info.png",
                                         record_pos=(-0.019, 0.219), resolution=(1125, 2436)))
            sleep(1)
            self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/login/step_longin.png",
                                         record_pos=(-0.004, 0.137), resolution=(1125, 2436)))


if __name__ == "__main__":
    unittest.main()

