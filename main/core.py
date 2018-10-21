# encoding: utf-8
# __author__ = "wyb"
# date: 2018/10/21
# 项目主逻辑
from main.timing import send_email
from threading import Thread


def main():
    t = Thread(target=send_email)
    t.start()
    print("主程序")