#!/usr/bin/env python3
#encoding:UTF-8
def oauth(consumer_key, consumer_secret, callback_url):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_url)
    redirect_url = auth.get_authorization_url()
    return redirect_url

import cgi
import cgitb
import textwrap
import io,sys
import json
import tweepy

# UnicodeEncodeErrorを防ぐ
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
cgitb.enable()

# jsonファイルからapiキーを読み込み
############################### 要変更 ###############################
# ローカル
json_open = open("./oauth_keys.json",'r')
#本番環境
#json_open = open("../oauth_keys.json",'r')
json_load = json.load(json_open)
consumer_key = json_load["consumer_key"]
consumer_secret = json_load["consumer_secret"]
############################### 要変更 ###############################
# ローカル用
callback_url = "http://localhost:8000/cgi-bin/twi_login.py"
# 本番用
#callback_url = "http://160.16.217.69/dresser/cgi-bin/twi_login.py"

print("Content-Type: text/html; charset=UTF-8\n\n")
print()
html ='''
<!DOCTYPE html>
<html lang = "ja">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">

<title>Dresser</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season" />
<meta name="keywords" content="dresser, fashion, coodinate, recommend, search, summer, tops, pants, onepiece, outwear" />
<meta name="author" content="Sechubai" />

<meta property="og:title" content="dresser"/>
<meta property="og:image" content="../images/dresser.jpg"/>
<meta property="og:site_name" content="dresser"/>
<meta property="og:description" content="Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season"/>

<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/animate.css">
<link rel="stylesheet" href="../css/bootstrap.css">
<link rel="stylesheet" href="../css/icomoon.css">
<link rel="stylesheet" href="../css/test.css">
<script type="text/javascript" src="../check.js"></script>
</head>

<body>
<div id="fh5co-wrap">
    <div class="large-div">
  	    <header id="fh5co-header">
		    <div class="container">
			    <div class="row">
				    <div class="col-md-4">
                        <h1 class="logo"><a href='./index.py'>Dresser</a></h1>
				    </div>
			    </div>
            </div>
	    </header>

	    <div class="fh5co-section">
		    <div class="container">
                <div class="row">
					<div class="col-md-6 col-md-push-3">
                        <div class="twitter_login">
                            <i class="icon-twitter"></i>
                            <b>Twitterでログイン</b>
                            <a class="link" href="{}"></a>
                        </div>
                    </div>

                            <!-- Twitterでログインするやつをかく -->
                            <form
                              action = "./login.py"
                              method = "post"
                              name = "myform"
                              onsubmit = "return check2();"
                            >

                    <div class="col-md-12">
                    </div>
                    <div class="middle-div col-md-6 col-md-push-3">
                        <div class="row">
                            <div class="col-md-6 col-md-push-3">
                                <h2>User ID</h2>
                                <input type = "text" class="form-control" name = "user_id" id='name' placeholder="User ID">
                            </div>
                            <div class="col-md-12">
                            </div>
                            <div class="col-md-6 col-md-push-3">
                                <h2>Password</h2>
                                <input type = "password" class="form-control" name = "password" minlength='8' id='pass' placeholder="Password">
                            </div>
                            <div class="top-space-50 col-md-12">
                                <div class="submit">
                                    <input type = "submit" value = "sign-in" class="btn btn-primary">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>
<footer id="fh5co-footer">
	<div class="container">
		<div class="row">
        <br>
        <br>
        <br>
            <div class="col-md-4">
				<h3>About Our App</h3>
				<p class="footer-font">Fashion Coordinates Recommender and Searching System Using Weather Forecast in Summer Season</p>
			</div>
            <div class="col-md-4">
				<h3>Member</h3>
				<p class="footer-font">
                Shingo Watanabe (Owner, Backend)<br>
                Tomoya Iwamoto (Member, Frontend)<br>
                Sho Shimamura (Member, Backend)<br>
                </p>
			</div>
        </div>
	</div>
</footer>

</body>
</html>
'''.format(oauth(consumer_key, consumer_secret, callback_url)).strip()

print(html)
