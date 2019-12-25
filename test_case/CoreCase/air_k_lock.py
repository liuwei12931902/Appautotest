# !/usr/bin/python
# -*- encoding = utf-8 -*-
# author: liuwei

import unittest
from airtest.core.api import *
from public.common.BaseApi import BaseMethod
from airtest.cli.parser import cli_setup
from config import globelsetting
from public.common.createlog import Runlogger
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
        self.runLog = Runlogger().debug_log()

    def tearDown(self):
        home()

    @recase(setUp, tearDown, 4)
    def test_lockserver(self):
        '''
        门锁用例失败,申请门锁按钮
        '''
        # self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/center/me.png",
        #                              record_pos=(0.383, 0.924), resolution=(1125, 2436)))
        # sleep(1)
        # self.driver.p_swipe([0.5, 0.8], [0.5, 0])
        # self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/center/swichloadlord.png",
        #                              record_pos=(-0.002, 0.774), resolution=(1125, 2436)))
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/center/server.png",
                       record_pos=(0.003, 0.928), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/center/lockdoor.png",
                       record_pos=(-0.358, -0.716), resolution=(1125, 2436)))
        # assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/center/lockintr.png",
        #                        record_pos=(-0.0, -0.026), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/center/lockbutton.png",
                       record_pos=(-0.011, 1.013), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/center/back.png",
                       record_pos=(-0.431, -0.908), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/center/back.png",
                       record_pos=(-0.431, -0.908), resolution=(1125, 2436)))
        # sleep(1)
        # self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/center/me.png",
        #                              record_pos=(0.383, 0.924), resolution=(1125, 2436)))
        # sleep(1)
        # self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/center/swicthtenant.png",
        #                              record_pos=(-0.004, 0.778), resolution=(1125, 2436)))


if __name__ == "__main__":
    unittest.main()
