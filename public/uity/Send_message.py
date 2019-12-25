#!/usr/bin python
# -*- coding:utf-8 -*-
# author: liuwei

import paramiko
import time
from config import globelsetting


class SendMessage(object):
    def __init__(self, Case):
        self.ssh_host = '10.0.0.221'
        self.ssh_port = 22
        self.username = 'xztest'
        self.password = '7c5cb6e5320e6c47f227841c'
        self.phone_number = ["13691422660", "18710463392", "15810216327", "15933678685", "18301448312", "18500361743",
                             "13436961715", "18844195352", "13910725671", "18210023150", "15810501841", "17744408687",
                             "15311809338", "15600655599"]
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


