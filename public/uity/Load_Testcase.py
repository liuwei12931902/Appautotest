#!/usr/bin python
# -*- coding:utf-8 -*-
# author: liuwei

import requests
import re
from bs4 import BeautifulSoup
import lxml


class read_case(object):
    global ss
    ss = requests.session()

    def login(self):
        url = 'http://testlink.xiaozhu.com/login.php?viewer='
        data = {
            'CSRFName': 'CSRFGuard_1333540185',
            'CSRFToken': 'da7a1be606ee8b177d3f70035a734c323c514568d5381e86ad03b52700e4d2dd4361afddd98d3805f30c09a919eaa5ed9cda0edf8adb917ab91d992c236e439f',
            'reqURI': '',
            'destination': '',
            'tl_login': 'liuwei',
            'tl_password': 'sbkill1rqlb6x',
        }
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }
        r = ss.post(url, headers=header, data=data)
        return r.cookies

    def screen_case(self, case_id):
        url = 'http://testlink.xiaozhu.com/lib/testcases/archiveData.php'
        data ={
            'version_id': 'undefined',
            'edit': 'testcase',
            'id': case_id,
            'form_token': '2075365980',
        }
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }
        r = ss.post(url, headers=header, data=data)
        page = r.text
        # soup = BeautifulSoup(page, 'lxml')
        # dict ={}
        # soup.find_all(,attrs={onclick:'launchEditStep(31)'})
        print(page)


if __name__ == "__main__":
    s = read_case()
    s.login()
    s.screen_case(29)
