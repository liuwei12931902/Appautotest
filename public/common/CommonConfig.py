# !/usr/bin/env python
# -*- ending:utf-8 -*-
# author: liuwei


from datetime import datetime


class CommonConfig(object):
    """
    通用配置文件
    """
    def baseUrl(self):
        return ''

    def getCurrentTime(self):
        format = '%Y-%m-%d %H:%M:%S'
        return datetime.now().strftime(format)

    def timeDiff(self, starttime, endtime):
        format = '%Y-%m-%d %H:%M:%S'
        return datetime.strftime(endtime, format) - datetime.strftime(starttime, format)

# **************************
# cc = CommonConfig()
# print(cc.getCurrentTime())
# **************************


