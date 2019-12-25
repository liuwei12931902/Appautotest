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
    def test_detailload(self):
        '''
        房源详情页加载
        :return:
        '''
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/seachButton.png",
                                     record_pos=(0.323, -0.6), resolution=(1125, 2436)))
        sleep(1)
        self.driver.p_click([0.5, 0.4051724137931034])
        assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/asserthouse.png",
                               record_pos=(-0.304, 0.918), resolution=(1125, 2436)), "进入了房源详情页")
        sleep(1)
        self.driver.p_swipe([0.5, 0.8], [0.5, 0])
        sleep(1.5)
        self.driver.p_swipe([0.5, 0.8], [0.5, 0])
        sleep(1.5)
        self.driver.p_swipe([0.5, 0.8], [0.5, 0])
        sleep(1.5)
        self.driver.p_swipe([0.5, 0.8], [0.5, 0])
        sleep(1.5)
        self.driver.p_swipe([0.5, 0.8], [0.5, 0])
        sleep(1.5)

    @recase(setUp, tearDown, 4)
    def test_picload(self):
        '''
        房源大图浏览模式
        :return:
        '''
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/seachButton.png",
                                     record_pos=(0.323, -0.6), resolution=(1125, 2436)))
        sleep(1)
        self.driver.p_click([0.5, 0.4051724137931034])
        assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/asserthouse.png",
                               record_pos=(-0.304, 0.918), resolution=(1125, 2436)), "进入了房源详情页")
        sleep(1)
        self.driver.p_click([0.5, 0.1539408866995074])
        sleep(1)
        self.driver.p_click([0.5, 0.1539408866995074])
        sleep(1)
        self.driver.p_swipe([0.5, 0.5], [0.0, 0.5])

    @recase(setUp, tearDown, 4)
    def test_collect(self):
        '''
        收藏用例
        '''
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/seachButton.png",
                                     record_pos=(0.323, -0.6), resolution=(1125, 2436)))
        sleep(1)
        self.driver.p_click([0.5, 0.4051724137931034])
        assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/asserthouse.png",
                               record_pos=(-0.304, 0.918), resolution=(1125, 2436)), "进入了房源详情页")
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/detailpage/collect.png",
                                     record_pos=(-0.236, 0.913), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/detailpage/selectcollect.png",
                                     record_pos=(-0.328, 0.556), resolution=(1125, 2436)))
        sleep(2)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/detailpage/save.png",
                                     record_pos=(0.003, 0.948), resolution=(1125, 2436)))
        sleep(1)
        assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/detailpage/assertcollect.png",
                               record_pos=(-0.236, 0.921), resolution=(1125, 2436)), "收藏成功")
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/detailpage/assertcollect.png",
                                     record_pos=(-0.236, 0.921), resolution=(1125, 2436)))

    @recase(setUp, tearDown, 4)
    def test_collect(self):
        '''
        收藏用例失败
        :return:
        '''
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/seachButton.png",
                                     record_pos=(0.323, -0.6), resolution=(1125, 2436)))
        sleep(1)
        self.driver.p_click([0.5, 0.4051724137931034])
        assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/asserthouse.png",
                               record_pos=(-0.304, 0.918), resolution=(1125, 2436)), "进入了房源详情页")
        sleep(1)


if __name__ == "__main__":
    unittest.main()
