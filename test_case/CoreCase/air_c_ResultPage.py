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
    def test_swipelist(self):
        '''
        进入搜索结果页，加载正常
        :return:
        '''
        try:
            self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/seachButton.png", record_pos=(0.323, -0.6), resolution=(1125, 2436)))
            sleep(1)
            assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/assertseach.png", record_pos=(0.172, -0.906), resolution=(1125, 2436)), "请填写测试点")
            self.driver.p_swipe([0.5, 0.8], [0.5, 0])
            sleep(1)
            self.driver.p_swipe([0.5, 0.8], [0.5, 0])
            sleep(1)
            self.driver.p_swipe([0.5, 0.8], [0.5, 0])
            sleep(1)
            self.driver.p_swipe([0.5, 0.8], [0.5, 0])
            sleep(1)
            self.driver.p_swipe([0.5, 0.8], [0.5, 0])
        except Exception as e:
            self.runLog.error(f'列表页加载失败{e}')
            raise e

    @recase(setUp, tearDown, 4)
    def test_sendtest(self):
        try:
            self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/seachButton.png",
                                         record_pos=(0.323, -0.6), resolution=(1125, 2436)))
            sleep(1)
            self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/home.png",
                                         record_pos=(-0.138, -0.711), resolution=(1125, 2436)))
            sleep(1)
            assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/homeassert.png",
                                   record_pos=(-0.144, -0.713), resolution=(1125, 2436)), "请填写测试点")
            sleep(1)
            self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/homeassert.png",
                                         record_pos=(-0.144, -0.713), resolution=(1125, 2436)))
            sleep(1)
            self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/localButton.png",
                                         record_pos=(-0.128, -0.802), resolution=(1125, 2436)))
            self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/tiananmen.png",
                                         record_pos=(-0.082, -0.732), resolution=(1125, 2436)))
            sleep(1)
            self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/confirmButton.png",
                                         record_pos=(-0.012, 0.924), resolution=(1125, 2436)))
            sleep(1)
            touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/xbutton.png",
                           record_pos=(0.299, -0.909), resolution=(1125, 2436)))
            # sleep(1)
            # assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/tiananmenassert.png", record_pos=(-0.134, -0.798), resolution=(1125, 2436)), "请填写测试点")
            # sleep(1)
            # self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/morescreen.png", record_pos=(0.111, -0.8), resolution=(1125, 2436)))
            # sleep(1)
            # self.driver.a_touch(Template(r"", record_pos=(-0.351, 0.139), resolution=(1125, 2436)))
            # sleep(1)
            # self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/Package.png", record_pos=(-0.012, 0.924), resolution=(1125, 2436)))
            # sleep(1)
            # assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/onescreen.png", record_pos=(0.118, -0.804), resolution=(1125, 2436)), "请填写测试点")
        except Exception as e:
            self.runLog.error(f'列表页筛选失败{e}')
            raise e

    @recase(setUp, tearDown, 4)
    def test_swich_map(self):
        '''
        切换地图页
        '''
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/seachButton.png",
                                     record_pos=(0.323, -0.6), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/swichmap.png",
                                     record_pos=(0.411, -0.909), resolution=(1125, 2436)))
        # sleep(1)
        # assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/assertmap.png",
        #                        record_pos=(-0.414, 1.039), resolution=(1125, 2436)), "切换地图成功")

        sleep(1)
        self.driver.p_swipe([0, 0.5], [0.5, 0.5])
        sleep(1)
        self.driver.p_swipe([0.5, 0.5], [0, 0.5])
        self.driver.p_pinch(direction=u'out')
        sleep(1)
        self.driver.p_pinch(direction=u'in')

    @recase(setUp, tearDown, 4)
    def test_swich_list(self):
        '''
        切换列表页
        :return:
        '''
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/seachButton.png",
                                     record_pos=(0.323, -0.6), resolution=(1125, 2436)))
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/swichmap.png",
                                     record_pos=(0.411, -0.909), resolution=(1125, 2436)))
        sleep(1)

        assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/assertmap.png",
                               record_pos=(-0.402, 1.05), resolution=(1125, 2436)), "切换到地图页")
        sleep(1)
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/swichlist.png",
                                     record_pos=(0.407, -0.906), resolution=(1125, 2436)))
        sleep(1)
        assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/assertseach.png",
                               record_pos=(0.164, -0.906), resolution=(1125, 2436)), "返回到列表页")

    @recase(setUp, tearDown, 4)
    def test_click_house(self):
        '''
        进入房源详情页失败
        '''
        self.driver.a_touch(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/seachButton.png",
                                     record_pos=(0.323, -0.6), resolution=(1125, 2436)))
        sleep(1)
        self.driver.p_click([0.5, 0.4051724137931034])
        assert_exists(Template(r"/Users/ios/Desktop/ios/ios-airtest/pagePic/corepic/resultpage/asserthouse.png",
                               record_pos=(-0.304, 0.918), resolution=(1125, 2436)), "进入了房源详情页")


if __name__ == "__main__":
    unittest.main()
