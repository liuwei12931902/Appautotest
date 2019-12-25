from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from config import globelsetting


def sendReportFile(file_path):
    # 读取路径
    sendfile = open(file_path, 'rb').read()
    msg = MIMEText(sendfile, _subtype='html', _charset='utf-8')
    msg['Content-Type'] = 'application/octet-stream'
    msg['Content-Disposition'] = 'attachment; filename = result.html'

    msgRoot = MIMEMultipart('related')
    # msgtext = MIMEText(content, _subtype='plain', _charset='utf-8')
    msgRoot.as_string(msg)

    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = ''
    msg['To'] = ''

    smtp = smtplib.SMTP('SMTP.163.com')
    smtp.set_debuglevel(1)
    smtp.login('l', '')
    smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())

    smtp.quit()
    print('test report has send out')


def newReport(testReport):
    lists = os.listdir(testReport)
    lists2 = lists.sort(reverse= True)
    # print(lists,lists2)
    return os.path.join(testReport, lists[1])

    # file_name = os.path.basename(file_new)


if __name__ == '__main__':
    f = newReport(globelsetting.report_path)
    print(f)
    # sendReportFile(f)
