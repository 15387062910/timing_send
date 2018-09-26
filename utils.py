# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/26
import shelve
from datetime import datetime

DATA_FILE = 'data/guestbook.dat'


def log(*args, **kwargs):
    print(*args, **kwargs)


def save_data(name, theme, content, create_time):
    """
    保存提交的数据
    :param name: 姓名
    :param theme: 评论主题
    :param content: 评论内容
    :param create_time: 评论时间
    :return:
    """
    database = shelve.open(DATA_FILE)
    # 获取数据库中已经存储的数据
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        greeting_list = database['greeting_list']
    # 添加提交的数据
    greeting_list.insert(0, {
        'name': name,
        'theme': theme,
        'content': content,
        'create_time': create_time
    })
    # 更新数据库
    database['greeting_list'] = greeting_list
    # 关闭数据库
    database.close()


def load_data():
    """
    返回已经提交的数据
    :return: 返回数据库中的数据
    """
    database = shelve.open(DATA_FILE)
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list


def get_ct():
    """
    生成当前时间 时间格式固定为%Y/%m/%d %H:%M:%S
    :return:
    """
    dt = datetime.now()
    ct = dt.strftime('%Y/%m/%d %H:%M:%S')
    # log(ct)
    return ct