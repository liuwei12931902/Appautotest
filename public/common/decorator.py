# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# author: liuwei


from functools import wraps
import time
from public.uity.Send_message import SendMessage


# class AdornCase(object):
#     '''
#     功能：实现用例执行失败后，再次执行，
#     连续失败3次后触发短信报警
#     '''
#     def __init__(self):
#         self.s =s
#         self.t =t
#         self.times =times
#
#     def __call__(self, func):
#         def wrapper(*a, **w):
#             for i in range(1, self.times):
#                 try:
#                     print('-------------------\nNum:', i)
#                     re = func(*a)
#                     print('success \n-------------------')
#                     return re
#                 except Exception:
#                     print('have a error ')
#                     self.s()
#                     self.t()
#                     print('\n-------------------')
#         raise Exception
#         return wrapper


def recase(s, t, n):
    def decorator(func):

        def wrapper(*a, **w):
            for i in range(1, n):
                try:
                    re = func(*a, **w)
                    print('--------------sussess---------------------')
                    return re
                except Exception:
                    print('have a error')
                    t(*a, **w)
                    s(*a, **w)
                    print('-------------faild---------------------')
                if i == 3:
                    print('begin')
                    name = str(func.__doc__)
                    print(name)
                    case = '【ios自动化测试报警】:'+name.replace('\n', '').replace(' ', '')
                    print(case)
                    send = SendMessage(Case=case)
                    time.sleep(4)
                    send.sendmessage()
                    print('end')
            raise Exception
        return wrapper
    return decorator
