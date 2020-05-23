from bs4 import BeautifulSoup, NavigableString
from bs4 import UnicodeDammit
import glob
import re
import bs4
import urllib.request
import datetime
import csv
import os.path
from datetime import date
import os
from random import seed
from random import randint
import time
import requests
from fake_useragent import UserAgent
from django.utils.html import strip_tags
ua = UserAgent()
now = (date.fromtimestamp(time.time()))
now = now.strftime('%Y-%m-%d')
now_subject = (datetime.datetime.now())
now_subject = now_subject.strftime('%m-%d')


proxies = {
	'http': 'socks5://x0506967:h9JWhEtghn@proxy-nl.privateinternetaccess.com:1080',
	'https': 'socks5://x0506967:h9JWhEtghn@proxy-nl.privateinternetaccess.com:1080',
	}

s = requests.Session()
header = {'User-Agent':str(ua.random)}
cookie_url = 'http://kcna.kp/kcna.user.home.retrieveHomeInfoList.kcmsf'
r = requests.get(cookie_url)
cookies_id = r.cookies['JSESSIONID']
cookies = {'JSESSIONID' : cookies_id}

kcna_article_list = []

page_dictionary = {
	'One' 	: '0',
	'Two' 	: '10',
	'Three' : '20',
	'Four' 	: '30',
	'Five' 	: '40',
	'Six' 	: '50',
	}
one_pages 	= ['One']#, 'Two', 'Three', 'Four', 'Five', 'Six']
three_pages	= ['One', 'Two', 'Three']#, 'Four', 'Five', 'Six']
all_pages 	= ['One', 'Two', 'Three', 'Four', 'Five', 'Six']

codes_list = []
for page in three_pages:
	time.sleep(15)
	print()
	print('------------------------------')
	print("Latest News Page: {}".format(page))
	DATA_LIST = {
		'article_code'		: '',
		'article_type_list'	: '',
		'news_type_code'	: 'NT41',
		'show_what' 		: 'L',
		'mediaCode' 		: '',
		'lang' 				: '',
		'page_start' 		: page_dictionary[page],
		'kwDispTitle'		: '',
		'keyword'			: '',
		'newsTypeCode'		: '',
		'articleTypeCode'	: '',
		'articleTypeList'	: '',
		'photoCount'		: '0',
		'movieCount'		: '0',
		'kwDispTitle'		: '',
		'kwContent'			: '',
		'fromDate'			: '',
		'toDate'			: '',
		}
	news_pull = s.post(url = 'http://kcna.kp/kcna.user.article.retrieveArticleListEaPage.kcmsf', data = DATA_LIST, proxies=proxies, cookies=cookies, headers=header)
	news_pull = news_pull.text
	codes_temp = news_pull.split('</articleCode>')
	code_count = len(codes_temp)
	codes_temp = codes_temp[0:10]
	for code_temp in codes_temp:
		code_temp = code_temp.split('CDATA[')
		code_temp = code_temp[1]
		code_temp = code_temp.split(']')
		code_temp = code_temp[0]
		codes_list.append(code_temp)

for code in codes_list:
	time.sleep(15)
	print("Working on article " + code)
	URL = 'http://kcna.kp/kcna.user.special.getArticlePage.kcmsf'
	LANGUAGE 		= 'eng'
	kwContent 		= '' #appears to be an unused variable in KCNA database, always lists as a blank value
	ARTICLETYPELIST = ''
	NEWSTYPECODE 	= 'NT00'
	SHOWWHAT 		= 'L'
	MEDIACODE 		= ''

	DATA = {
		'article_code'		: code,
		'article_type_list'	: ARTICLETYPELIST,
		'news_type_code'	: NEWSTYPECODE,
		'show_what' 		: SHOWWHAT,
		'mediaCode' 		: MEDIACODE,
		'lang' 				: LANGUAGE,
			}

	news_pull = s.post(url = URL, data = DATA, proxies=proxies, cookies=cookies, headers=header)

	full_response = news_pull.text

	article_soup = BeautifulSoup(full_response, 'html.parser')

	content = 	article_soup.find("input", {"id" : "content"})
	content = 	content.get('value')
	content =  	strip_tags(content)
	title 	= 	article_soup.find("input", {"id" : "mainTitle"})
	title 	= 	title.get('value')
	title 	= 	strip_tags(title)
	date 	= 	article_soup.find("input", {"id" : "fCreateDate"})
	date 	= 	date.get('value')
	date 	= 	strip_tags(date)
	article_instance = [title, date, content]
	if date == now:
		kcna_article_list.append(article_instance)

print("---------------------------------")
print("Article collection finished")
print()


#	print(title.get('value'))
#	print(date.get('value'))
#	print(content.get('value'))


body_list = []
html = """\
<html>
	<head>
	<style type="text/css">

 	p {font-size: 12px; color: black !important; font-family: "Open Sans", sans-serif; line-height: 1; margin-bottom: 0px; margin-top: 0px; padding-bottom: 0px; padding-top: 0px;}
    a:link {font-family: "Open Sans", sans-serif; font-size: 30px; color: #003b63; line-height: 30px; text-align: center; margin-top: 25px;  text-decoration: none;}
    a {font-family: "Open Sans", sans-serif; font-size: 30px; line-height: 30px; text-align: center; margin-top: 25px;  text-decoration: none;}
    a:visited {font-family: "Open Sans", sans-serif; font-size: 30px; line-height: 30px; text-align: center; margin-top: 25px; text-decoration: none;}
	h1 {color: white; font-family: "Open Sans", sans-serif; font-size: 35px; line-height: 35px;margin-bottom: 0px; margin-top: 0px; padding-bottom: 0px; padding-right: 5px; padding-left: 10px;background-color: #003b63; height: 40px;}
	h3 {font-family: "Open Sans", sans-serif; font-size: 30px; line-height: 10px; text-align: center; margin-top: 25px;}
	h4 {font-family: "Open Sans", sans-serif; font-size: 25px; line-height: 25px; margin-bottom: 0px; margin-top: 0px; padding-bottom: 0px; padding-top: 5px;}
	h5 {font-family: "Open Sans", sans-serif; font-size: 15px; line-height: 1.5; font-weight: 600; margin-bottom: 0px; margin-top: 0px; padding-bottom: 0px; padding-top: 10px;}
	h6 {font-family: "Open Sans", sans-serif; font-size: 25px; line-height: 25px; margin-bottom: 0px; margin-top: 10px; padding-bottom: 0px; padding-top: 5px; border-top: 2px solid rgba(0, 0, 0, 0.27); }


   </style>

 	</head>
 	<body>
	<div>
"""

html = html + """
    	<h1>DPRK Media: {}</h1>
    </div>
    <br>
    <p font-size:13><i>This daily report is brought to you by the Korea Data History Initiative (KDHI) of the Korea Studies program at the Johns Hopkins School of Advanced International Studies. <br><br>All media presented in the report is written by the Democratic People's Republic of Korea (DPRK). KDHI's DPRK State Media Report is intended solely for research purposes and not the consumption of objective news. </i></p>
	<h6> KCNA Articles</h6>

""".format(now_subject)


html_end = """\
	<br>
	<br>
	<div>
    	<h3><a href="kdhi.us">KDHI</a></h3>
    </div>
    </body>
</html>
"""
body_list_kcna = []
email_content = html
for article_kcna in kcna_article_list:
	article_strings = '<h5>'
	article_strings = article_strings + article_kcna[0]
	article_strings = article_strings + '</h5>'
	article_strings = article_strings + article_kcna[1]
	body_list_kcna.append(article_strings)
for formatted_article in body_list_kcna:
	for item in formatted_article:
		email_content += item

email_content += html_end


import smtplib
import email.message
gmail_user = 'kdhinews@gmail.com'
gmail_password = 'gwncdxscvkjamthy'


msg = email.message.Message()
msg['Subject'] = "KDHI's DPRK State Media Report for " + now


msg['From'] = gmail_user
msg['To'] = 'kdhinews@gmail.com'
recipients = ['crosbysn@gmail.com']
msg.add_header('Content-Type', 'text/html')
msg.set_payload(email_content)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
# Login Credentials for sending the mail
server.login(msg['From'], gmail_password)

for address in recipients:
    server.sendmail(msg['From'], address, msg.as_string())
