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
    def test_kepper(self):
        '''
        房东服务中心点击小猪管家，点击申请保洁按钮
        '''
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/center/server.png",
                       record_pos=(0.003, 0.928), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/xzkepper/xzkeeper.png",
                                     record_pos=(-0.12, -0.711), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/xzkepper/applybutton.png",
                                     record_pos=(-0.0, 0.939), resolution=(1125, 2436)))
        assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/xzkepper/assertkepper.png",
                               record_pos=(0.008, -0.911), resolution=(1125, 2436)),
                      "进入选择地址和房源页")


if __name__ == "__main__":
    unittest.main()
