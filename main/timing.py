# encoding: utf-8
# __author__ = "wyb"
# date: 2018/10/21
# 实现定时功能
# 发送邮件
# 每天早上8点发送邮件
# 发送内容: 	前一天所有的用户反馈内容
import time
import schedule
from main import mail
from private.get import get_laf_advice

# # 定时设置
# HOUR = 0     # 定时小时
# MIN = 13     # 定时分钟
# SEC = 13     # 定时秒
#
#
# def _timing_send():
#     current_time = time.localtime(time.time())                          # 当前时间date
#     cur_time = time.strftime('%H%M', time.localtime(time.time()))       # 当前时间str
#     if current_time.tm_hour == HOUR and current_time.tm_min == MIN and current_time.tm_sec == SEC:
#         print("START")
#         content = _email_content()
#         mail.send_email(content)
#         print(cur_time)
#     time.sleep(1)


# 测试定时发送
def _email_content():
    # content = "这是一封定时发送的邮件，定时发送于{}:{}:{}".format(HOUR, MIN, SEC)
    content = "这是一封定时发送的邮件，定时发送于23:15"
    return content


# 测试定时发送
def _send():
    content = _email_content()
    mail.send_email(content)


# 真正的建议发送
def send():
    advice = get_laf_advice()
    mail.send_email(advice)


def send_email():
    print("schedule")
    schedule.every().day.at("23:15").do(_send)
    # schedule.every().day.at("23:15").do(send)

    while True:
        schedule.run_pending()
