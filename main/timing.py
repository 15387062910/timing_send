# encoding: utf-8
# __author__ = "wyb"
# date: 2018/10/21
# 实现定时功能
# 定时发送邮件 - 每天xx点xx分发送邮件
# 发送内容: 	前一天所有的用户反馈内容
import schedule
from main import mail
from private.get import get_laf_advice


# 建议发送
def send():
    advice = get_laf_advice()
    mail.send_email(advice)


# 定时某一时刻发送
def send_email():
    print("schedule")
    schedule.every().day.at("23:48").do(send)

    while True:
        schedule.run_pending()
