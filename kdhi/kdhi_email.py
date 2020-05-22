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


proxies = {
	'http': 'socks5://x0506967:h9JWhEtghn@proxy-nl.privateinternetaccess.com:1080',
	'https': 'socks5://x0506967:h9JWhEtghn@proxy-nl.privateinternetaccess.com:1080',
	}

s = requests.Session() 


'''
#---------------PAGE ONE (Sepperated to simulate how users would ping system by using two different request function types)}
print("Latest News Page: 1")
DATA_LIST = {
	}
news_pull = s.post(url = 'http://kcna.kp/kcna.user.article.retrieveNewsViewInfoList.kcmsf', data = DATA_LIST, proxies=proxies)
news_pull = news_pull.text
news_pull_soup = BeautifulSoup(news_pull, 'html.parser')
left_article = news_pull_soup.find("div", {"class" : "left_articles"})

for article_box in left_article.find_all('li'):
	on_click = (article_box.a['onclick'])
	code_list = on_click.split('"')
	code = code_list[1]
	print(code)
'''
page_dictionary = {
	'One' 	: '0',
	'Two' 	: '10',
	'Three' : '20',
	'Four' 	: '30',
	'Five' 	: '40',
	'Six' 	: '50',
	}
english_pages = ['One']#, 'Two', 'Three', 'Four', 'Five', 'Six']
'''
codes_list = []
for page in english_pages:
#---------------PAGE TWO
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

	news_pull = s.post(url = 'http://kcna.kp/kcna.user.article.retrieveArticleListEaPage.kcmsf', data = DATA_LIST, proxies=proxies)
	news_pull = news_pull.text
	codes_temp = news_pull.split('</articleCode>')
	code_count = len(codes_temp)
	codes_temp = codes_temp[0:10]
	for code_temp in codes_temp:
		code_temp = code_temp.split('CDATA[')
		code_temp = code_temp[1]
		code_temp = code_temp.split(']')
		code_temp = code_temp[0]
		print(code_temp)
		codes_list.append(code_temp)


	for article_box in left_article.find_all('li'):
		on_click = (article_box.a['onclick'])
		code_list = on_click.split('"')
		code = code_list[1]
		print(code)
	'''
#for article_code_str in codes_list:
DATA_LIST = {
		'article_code'	: 'AR0135953',
		'kwContent:' 	: '',
		'article_type_list'	: '',
		'news_type_code'	: 'NT00',
		'show_what' 		: 'L',
		'mediaCode' 		: '',
		'lang' 				: '',
		}
article_pull = s.post(url = 'http://kcna.kp/kcna.user.special.getArticlePage.kcmsf', data = DATA_LIST, proxies=proxies)
print(article_pull.text)
