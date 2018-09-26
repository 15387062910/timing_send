# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/18
from flask import Flask, request, render_template, redirect, escape, url_for
from utils import save_data, load_data, log, get_ct
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    data_list = load_data()
    return render_template("index.html", comments=data_list)


@app.route("/post", methods=['post'])
def post():
    """
       用于提交评论的URL
    :return:
    """
    name = request.form.get('name', '')
    theme = request.form.get('theme', '')
    content = request.form.get('content', '')
    create_time = get_ct()
    log(name, theme, content, create_time)
    # 保存数据
    save_data(name, theme, content, create_time)

    return redirect('/')


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='127.0.0.1',
        port=8888,
    )
    app.run(**config)
