# /usr/bin/python
# -*- coding:utf-8 -*-
# author: liuwei


"""
功能：
1，自动提交bug 到 bugfree
2，监控bug报告，出现error 则触发
3，分模块提交给各负责人
"""

import requests
import re


class SubmitBug(object):

    global ss
    ss = requests.session()

    def login(self):
        ss.keep_alive = False
        url = 'http://bugfree.xiaozhu.com/site/login'
        data = {
            'LoginForm[username]': '',
            'LoginForm[password]': '',
            'LoginForm[language]': 'zh_cn',
            'LoginForm[rememberMe]': '0'
        }
        header= {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }
        r = ss.post(url, headers=header, data=data)
        return r.cookies

    def submitbug(self,title, user, severity, repeat_step):
        url = 'http://bugfree.xiaozhu.com/info/edit?type=bug&action=opened&product_id=10'
        bugtitle = f'【ios】【{title}】测试自动化发送bug'
        assign_to_name = {
            'user': '',
            'user1': '',
            'user2': '',
            'user3': '',
            'user4': '',
            'user5': '',
            'user6': '',
            'user7': '',
            'user8': '',
        }
        data= {
            'BugInfoView[deleted_file_id]': '',
            'BugInfoView[lock_version]': '',
            'BugInfoView[product_id]': '10',
            'isPageDirty': '',
            'templateTitle': '',
            'BugInfoView[title]': '',
            'layer1_module': '0',
            'BugInfoView[productmodule_id]': '0',
            'BugInfoView[assign_to_name]': '',
            'BugInfoView[mail_to]': '',
            'BugInfoView[severity]': '',
            'BugInfoView[priority]': '',
            'BugInfoView[related_bug]': '',
            'BugInfoView[related_case]': '',
            'BugInfoView[related_result]': '',
            'attachment_file[]': '(binary)',
            'BugInfoView[action_note]':'',
            'BugInfoView[repeat_step]': '',
        }
        data['BugInfoView[title]'] = bugtitle
        data['BugInfoView[assign_to_name]'] = assign_to_name[user]
        data['BugInfoView[severity]'] = severity
        data['BugInfoView[repeat_step]'] = repeat_step
        ss.post(url, data=data)
        print(ss.cookies)

# *********************************************************************
# 调用方法
# s = SubmitBug()
# s.login()
# s.submitbug('ios', 'user8', '1', '<span style="color:#545454;font-family:font-weight:700;white-space:pre-wrap;">bug复现步骤</span><br />')
# *********************************************************************
