#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


def send_email(receivers_list, content):
    mail_host = "smtp.163.com"  # 设置服务器网易163
    mail_user = '18530983738@163.com'  # 用户名
    mail_pass = 'fbwmfchtrsflvxqf'  # 口令
    sender = '18530983738@163.com'
    # receivers = ['', ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText(content, 'plain', 'utf-8')  # 内容
    message['From'] = formataddr(['抽屉新热榜', sender])
    subject = '抽屉新热榜注册'
    message['Subject'] = Header(subject, 'utf-8')  # 主题

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers_list, message.as_string())
        return 'success'
    except smtplib.SMTPException:
        return 'error'

'''
def email(email_list, content, subject='抽屉新热榜-用户注册'):
    mail_host = "smtp.163.com"  # 设置服务器网易163
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = formataddr(['抽屉新热榜', '18530983738@163.com'])
    msg['Subject'] = subject

    server = smtplib.SMTP(mail_host, 25)
    server.login('18530983738@163.com', 'fbwmfchtrsflvxqf')
    server.sendmail('18530983738@163.com', email_list, msg.as_string())
'''



if __name__ == "__main__":
    ret = send_email('627904863@qq.com', 'slkj')
    print(ret)
    # email(['627904863@qq.com', ], 'sfasdf')
