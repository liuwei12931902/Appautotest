#!/usr/bin python
# -*- coding:utf-8 -*-
# author: liuwei

import paramiko
import time
from config import globelsetting


class SendMessage(object):
    def __init__(self, Case):
        self.ssh_host = ''
        self.ssh_port = 22
        self.username = ''
        self.password = ''
        self.phone_number = []
        self.content = Case

    def connectxztest(self):
        connection = paramiko.Transport((self.ssh_host, self.ssh_port))
        connection.connect(username=self.username, password=self.password)
        ssh = paramiko.SSHClient()
        ssh._transport = connection
        return ssh

    def sendmessage(self):
        ssh = SendMessage.connectxztest(self)
        for i in range(len(self.phone_number)):
            stdin, stdout, stderr = ssh.exec_command(
                "php /var/lib/jenkins/workspace/test-remindclient-00/script/"
                "test/testSMS.php " + self.phone_number[i] + ' ' + self.content)
            print(stdout.read().decode())
            time.sleep(5)
            # print('sussess')

# ********************
#   使用方法
#  sendmessage = SendMessage()
#  sendmessage.sendmessage()
# ********************


