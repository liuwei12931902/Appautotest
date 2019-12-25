# Appautotest
# 框架简介
基于Airtest框架demo ，适用于App自动化测试，环境搭建参考https://airtest.doc.io.netease.com/


# 各文件类作用 简介
├── app                      # ipa/apk 存放路径

├── config                   # 配置文件路径

│   ├── __init__.py

│   ├── globelsetting.py    # 全局配置文件读取

│   └── setting.ini         # 配置文件

├── datadriver               # 测试数据路径

│   └── __init__.py

├── public                   # 公共方法类

│   ├── __init__.py

│   ├── common               # 通用方法类

│   │   ├── BaseApi.py       # Airtest方法的重新封装

│   │   ├── CommonConfig.py  # 配置文件类

│   │   ├── InstallApp.py    # 安装卸载方法

│   │   ├── Readsetting.py   # 读取配置文件方法

│   │   ├── TsetCaseInfo.py  # 测试用例信息类

│   │   ├── __init__.py

│   │   ├── createlog.py     # 创建日志方法

│   │   ├── decorator.py     # 装饰器类用于 重跑和监控 

│   │   └── readExcel.py     # 读取测试数据

│   └── uity                 # 工具类

│       ├── AutoSubmitBug.py # 自动提交bug致bugfree

│       ├── DownloadApp.py   # 下载安装包fir.im

│       ├── Load_Testcase.py # 读取测试用例

│       ├── Send_Mail.py     # 发送 邮件

│       ├── Send_message.py  # 发送 短息

│       ├── __init__.py

├── run_all_case.py         # 执行文件

├── runner

│   ├── __init__.py

│   └── run.sh              # shell执行文件

├── test_case               # 测试用例文件

│   ├── CoreCase          	# 核心测试用例文件

│   │   ├── __init__.py

│   │   ├── __pycache__

│   │   ├── air_a_RegisterLogin.py

│   │   └── air_b_Discover.py

│   ├── HighLevelCase      # 高级测试用例文件

│   │   ├── __init__.py

│   ├── MiddleCase         # 测试中级用例文件

│   │   ├── __init__.py

└── test_report			   # 测试报告

    ├── HTMLReport
    
    │   └── __init__.py
    
    ├── __init__.py
    
    ├── log               # Airtest日志
    
    │   └── log.txt
    
    └── log-xz			  # 自己的日志
    
        ├── 2019-05-04.log
        
        └── __init__.py
