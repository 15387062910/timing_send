# encoding: utf-8
# __author__ = "wyb"
# date: 2018/10/21
# 发送邮件功能
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from private.settings import email_info, to_addr

import smtplib

sender_user = email_info["sender_user"]
sender_pwd = email_info["sender_pwd"]
smtp_server = email_info["smtp_server"]


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr('www.weyoung.co <%s>' % sender_user)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('LAF用户反馈', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(sender_user, sender_pwd)
    server.sendmail(sender_user, to_addr, msg.as_string())
    server.quit()

