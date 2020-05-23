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
ua = UserAgent()


proxies = {
	'http': 'socks5://x0506967:h9JWhEtghn@proxy-nl.privateinternetaccess.com:1080',
	'https': 'socks5://x0506967:h9JWhEtghn@proxy-nl.privateinternetaccess.com:1080',
	}

cookies = {'JSESSIONID' : '4A16CD357E94F83392716DBC11F2372C'}
s = requests.Session()
header = {'User-Agent':str(ua.random)}

page_dictionary = {
	'One' 	: '0',
	'Two' 	: '10',
	'Three' : '20',
	'Four' 	: '30',
	'Five' 	: '40',
	'Six' 	: '50',
	}
english_pages = ['One']#, 'Two', 'Three', 'Four', 'Five', 'Six']

codes_list = []
for page in english_pages:
	print('''
		------------------------------''')
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
	title 	= 	article_soup.find("input", {"id" : "mainTitle"})
	title 	= 	title.get('value')
	date 	= 	article_soup.find("input", {"id" : "fCreateDate"})
	date 	= 	date.get('value')
#	print()
#	print("---------------------------------")
#	print(code)
#	print(title.get('value'))
#	print(date.get('value'))
#	print(content.get('value'))
