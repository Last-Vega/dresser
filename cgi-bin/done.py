#!/usr/bin/env python3
#encoding:UTF-8

def get_users_clothes(form, user, c):
    user_id = user
    TypeCategory = []
    for row in form.value:
        if row.value not in TypeCategory:
            TypeCategory.append(row.value)
    TypeCategory = ','.join(TypeCategory)
    c.execute('INSERT INTO users_clothes VALUES (?,?)', (user_id, TypeCategory) )
    # データベースに変更加えたらコミットしないといけないらしい
    conn.commit()

#---------------------------------------------
# プログラム本体
#---------------------------------------------
import cgi
import cgitb
import sqlite3
import textwrap
import json
import sys
import requests
import re
from http import cookies
import os
import hashlib
import io,sys
# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
form = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE",""))

#user_id = form['user_id'].value
user = cookie['user'].value
cgitb.enable()
conn = sqlite3.connect('./clothes/dresser.db')
c = conn.cursor()
# クッキーを生成しuser_id を遷移先のページに渡す
print("Set-Cookie: user="+ user)
print("Content-Type: text/html; charset=UTF-8\n\n")

html = textwrap.dedent('''
<!DOCTYPE html>
<html lang = "ja">
<head>
<title>Dresser</title>
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/animate.css">
<link rel="stylesheet" href="../css/bootstrap.css">
<link rel="stylesheet" href="../css/icomoon.css">
</head>
    
<body style="background-color: #ffefd5;">
    <div class="fh5co-section">
		<div class="container">

			<div class="row">
				<div class="col-md-12">
                    <h1>Update Completed!</h1>
                </div>
                <div class="col-md-12">
                    <h3>Your account was created! </h3>
                </div>
                <div class="col-md-12">
                    <h3>You can enjoy our APP! </h3>
                </div>
            </div>
        </div>
    </div>

    </body>
    <div class="fh5co-section">
		<div class="container">

			<div class="row">
				<div class="col-md-12">
                    <a href='./index.py'>トップに戻る</a>
                </div>
            </div>
        </div>
    </div>
</html>
''').strip()
print(html)
get_users_clothes(form, user, c)
