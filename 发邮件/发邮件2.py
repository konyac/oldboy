#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器网易163
mail_user = "18530983738@163.com"  # 用户名
mail_pass = "fbwmfchtrsflvxqf"  # 口令

sender = '18530983738@163.com'
receivers = ['627904863@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')#发件人
# message['To'] = Header("测试", 'utf-8')#收件人

message['From']='18530983738@163.com'
message['To']='627904863@qq.com'

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8') #主题

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
