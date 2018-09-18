# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/18
import shelve
from flask import Flask, request, render_template, redirect, escape

app = Flask(__name__)


def save_data(name, comment, create_time):
    pass


def load_data():
    pass


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='127.0.0.1',
        port=8888,
    )
    app.run(**config)
