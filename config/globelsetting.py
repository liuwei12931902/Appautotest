# !/usr/bin/python
# -*- encoding:utf-8 -*-
# author: liuwei


import os
from public.common.Readsetting import ReadSetting


# 读取配置文件
# 获取srtting路径
file_path = os.path.split(os.path.realpath(__file__))[0]


# 读取setting.ini 文件
read_config = ReadSetting(os.path.join(file_path, 'setting.ini'))


# 通过setting.ini获取项目参数
project_path = read_config.getsettingvalues('project', 'project_path')


# app存放路径
app_path = os.path.join(project_path, 'app')

# 日志生成路径
log_path = os.path.join(project_path, 'test_report/log-xz')

# air日志路径
alog_path = os.path.join(project_path, 'test_report/log')

# 核心测试用例路径
CoreCase_path = os.path.join(project_path, 'test_case/CoreCase')


# 高级测试用例路径
HighLevelCase_path = os.path.join(project_path, 'test_case/HighLevelCase')


# 中级测试用例路径
MiddleCase_path = os.path.join(project_path, 'test_case/MiddleCase')


# 测试数据路径
datadriver_path = os.path.join(project_path, 'datadriver')


# 核心测试图片路径
CorePic_path = os.path.join(project_path, 'pagePic/corepic')


# 高级测试图片路径
HighLevelPic_path = os.path.join(project_path, 'test_case/HighLevelPic')


# 测试报告路径
report_path = os.path.join(project_path, 'test_report/HTMLReport')


# 中级测试图片路径
MiddlePic_path = os.path.join(project_path, 'test_case/MiddlePic')

# 手机号列表
mobile_list = read_config.getsettingvalues('mobile', 'mobile_list')
