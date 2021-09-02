#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template

app = Flask (__name__)


@app.route ("/", methods=["GET", "POST"])
def home():
    return render_template ('home.html')


@app.route ("/login", methods=["GET"])
def login_form():
    return render_template('form.html')


@app.route ("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return render_template('login-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run ()
