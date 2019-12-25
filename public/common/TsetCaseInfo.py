# !/usr/bin/env python
# -*- ending:utf-8 -*-
# author: liuwei


class TestCaseInfo(object):
    def __init__(self, id='', name='', owner='', result='faild', starttime='', endtime='', errorinfo =''):
        self.id = id
        self.name = name
        self.owner = owner
        self.result = result
        self.starttime = starttime
        self.endtime = endtime
        self.errorinfo = errorinfo

