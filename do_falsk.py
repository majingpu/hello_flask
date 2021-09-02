#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request

app = Flask (__name__)


@app.route ("/", methods=["GET","POST"])
def home():
    return '<h1>hello flask</h1>'


@app.route ("/login", methods=["GET"])
def login_form():
    return '''<form action="/login" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route ("/login", methods=["POST"])
def login():
    # 需要从request对象读取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run ()
