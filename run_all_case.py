# !/usr/bin python
# -*- encoding= utf-8 -*-
# auther : liuwei


import unittest
import os
import time
from config import globelsetting
from HTMLTestRunner import HTMLTestRunner
from public.uity import Send_Mail


class TestRunner(object):

    def noreportrunner(self):
        """
        无报告执行方法
        :return:
        """
        testsunit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover('test_case', pattern='air*.py', top_level_dir=None)
        for test_suiet in discover:
            for test_case in test_suiet:
                testsunit.addTests(test_case)
        Runner = unittest.TextTestRunner()
        Runner.run(testsunit)

    def hasreportrunner(self):
        """
        有报告执行方法 ，并发送邮件
        :return:
        """
        discover = unittest.defaultTestLoader.discover('test_case', pattern='air*.py', top_level_dir=None)
        now = time.strftime('%Y-%m-%d-%H:%M:%S')
        report_html = os.path.join(globelsetting.report_path + '/'+now+'report.html')
        with open(report_html, 'wb') as f:
            Runner = HTMLTestRunner(stream=f, title='ios测试报告', description='测试结果')
            Runner.run(discover)
        new_report = Send_Mail.newReport(globelsetting.report_path)
        Send_Mail.sendReportFile(new_report)


if __name__ == "__main__":
    runner = TestRunner()
    runner.hasreportrunner()
