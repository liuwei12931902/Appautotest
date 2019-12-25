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
        # 创建设备对象

    def setUp(self):
        # 实例化日志类
        self.logger = Runlogger().debug_log()
        # 通过包名打开app
        start_app('xiaozhu.com.XZTenant')
        self.dirver = BaseMethod()
        sleep(2)

    def tearDown(self):
        home()

    @recase(setUp, tearDown, 4)
    def test_Load(self):
        '''
        发现首页发现页显示、加载
        '''

        assert_not_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/network_false.png",
                                   record_pos=(-0.004, -0.115), resolution=(1125, 2436)),"不存在网络加载失败")
        if exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/step_Alert.png",
                           record_pos=(0.422, -0.906), resolution=(1125, 2436))
                  ):
            self.dirver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/step_Alert.png", record_pos=(0.422, -0.906), resolution=(1125, 2436)))
        else:
            sleep(1)
            self.dirver.p_swipe([0.5, 0.8], [0.5, 0])
            sleep(1.5)
            self.dirver.p_swipe([0.5, 0.8], [0.5, 0])
            sleep(1.5)
            self.dirver.p_swipe([0.5, 0.8], [0.5, 0])
            sleep(1.5)

    # @recase(setUp, tearDown, 4)
    def test_StoryAndCityAndHousing(self):
        '''
        故事页城市房源详情页进入
        '''
        assert_not_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/network_false.png",
                                   record_pos=(-0.004, -0.115), resolution=(1125, 2436)),
                          "不存在网络加载失败")
        self.dirver.p_swipe([0.5, 0.85], [0.5, 0])
        sleep(2)
        self.dirver.p_swipe([0.5, 0.6], [0.5, 0])
        sleep(2)
        self.dirver.p_click([0.152, 0.14901477832512317])
        # self.dirver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/business.png",
        #                record_pos=(-0.336, -0.704), resolution=(1125, 2436)))2436
        self.dirver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/yunying_back.png",
                                     record_pos=(-0.432, -0.898), resolution=(1125, 2436)))
        sleep(1)
        self.dirver.p_click([0.5, 0.5283251231527094])
        assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/we_story.png",
                               record_pos=(-0.0, -0.901), resolution=(1125, 2436)), "请填写测试点")
        self.dirver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/yunying_back.png",
                                     record_pos=(-0.432, -0.898), resolution=(1125, 2436)))
        sleep(1)
        self.dirver.p_swipe([0.5, 0.4], [0.5, 0])
        sleep(2)
        self.dirver.p_click([0.456, 0.6225369458128078])
        sleep(1)

    @recase(setUp, tearDown, 4)
    def test_jumpReult(self):
        '''
        选择目的地，选择入住日期，点击搜索按钮
        '''
        self.dirver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/citybutton.png",
                                     record_pos=(-0.358, -0.156), resolution=(1125, 2436)))
        sleep(1)
        self.dirver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/beijing.png",
                                     record_pos=(-0.12, -0.385), resolution=(1125, 2436)))
        sleep(1)
        self.dirver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/seachbutton.png",
                                     record_pos=(-0.017, 0.209), resolution=(1125, 2436)))
        assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/discover/assertbeijing.png",
                               record_pos=(-0.267, -0.908), resolution=(1125, 2436)),
                      "跳转北京结果页")


if __name__ == "__main__":
    unittest.main()
