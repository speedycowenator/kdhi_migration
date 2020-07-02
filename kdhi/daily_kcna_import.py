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

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from media_archive.models import state_media_article, state_media_publication
from django.utils.html import strip_tags

ua = UserAgent()
now = (date.fromtimestamp(time.time()))
now = now.strftime('%Y-%m-%d')
now_subject = (datetime.datetime.now())
now_subject = now_subject.strftime('%m-%d')
kcna_article_list = []
def clear_character_junk(line):
	line = line.replace('\u2032', "'")
	line	= line.replace('\u2019', "'")
	line	= line.replace('\u2018', "'")
	line = line.replace('\u2012', "-")
	line = line.replace('\u2014', "-")
	line = line.replace('\u2015', "-")
	line = line.replace('\uff0d', "-")
	line = line.replace('\uff0d', "-")
	line = line.replace('\uff5e', "~")
	line = line.replace('\u2103', "(degrees celsius")

# Ordered number circles i.e. (1)
	line	= line.replace('\u2460', '(1)')
	line	= line.replace('\u2461', '(2)')
	line	= line.replace('\u2462', '(3)')
	line	= line.replace('\u2463', '(4)')
	line	= line.replace('\u2464', '(5)')
	line	= line.replace('\u2465', '(6)')
	line	= line.replace('\u2466', '(7)')
	line	= line.replace('\u2467', '(8)')
	line	= line.replace('\u2468', '(9)')
	line	= line.replace('\246a', '(11)')
	line	= line.replace('\246B', '(12)')
	line	= line.replace('\246c', '(13)')
	line	= line.replace('\246D', '(14)')
	line	= line.replace('\246e', '(15)')
	line	= line.replace('\246f', '(16)')
	line	= line.replace('\u2469', '(10)')
	line	= line.replace('\u2470', '(17)')
	line	= line.replace('\u2471', '(18)')
	line	= line.replace('\u2472', '(19)')
	line	= line.replace('\u2473', '(20)')
	line	= line.replace('\u2474', '(1)')
	line	= line.replace('\u201c', '"')
	line	= line.replace('\u201d', '"')
#Misc
	line 	= line.replace('\uff24', 'D')
	line 	= line.replace('\uff1f', '?')
	line 	= line.replace('\ufe56', '?')
	line 	= line.replace('\u3000', ' ')
	line	 = line.replace('\ufe16', '?')
	line	= line.replace("\t", '')
	line	= line.replace("\\t", '')
	line	= line.replace("\\", '')
	line	= line.replace('  ', ' ')
	line	= line.replace('\u300b', '')
	line	= line.replace('\u300a', '')
	line	= line.replace('\u2165', 'VI')
	line	= line.replace('\uff0c', ',')
	line	= line.replace('\u338f', 'kg')
	line	= line.replace('\u33a1', '(square meters')
	line	= line.replace('\u33a5', '(cubic meters)')
	line 	= line.replace('\uffe5', ' (Japanese Yen) ')
	line 	= line.replace(	'\u2026', '...')

	line	= line.replace('&quot;', '')
	line	= line.replace('nobr', '')
	line	= line.replace('strongfont', '')
	nonBreakSpace	= u'\xa0'
	line	= line.replace(nonBreakSpace, ' ')
	return(line)

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

page_dictionary = {
	'One' 	: '0',
	'Two' 	: '10',
	'Three' : '20',
	'Four' 	: '30',
	'Five' 	: '40',
	'Six' 	: '50',
	}
one_pages 	= ['One']#, 'Two', 'Three', 'Four', 'Five', 'Six']
three_pages	= ['One', 'Two']#, 'Three', 'Four', 'Five', 'Six']
all_pages 	= ['One', 'Two', 'Three', 'Four', 'Five', 'Six']

codes_list = []
for page in one_pages:
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
		'lang' 				: 'eng',
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
	time.sleep(60)
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
	
	full_response = news_pull.text

	article_soup = BeautifulSoup(full_response, 'html.parser')


	content = 	article_soup.find("input", {"id" : "content"})
	content = 	content.get('value')
	content =  	strip_tags(content)
	content = 	clear_character_junk(content)
	title 	= 	article_soup.find("input", {"id" : "mainTitle"})
	title 	= 	title.get('value')
	title 	= 	strip_tags(title)
	title 	= 	clear_character_junk(title)
	date 	= 	article_soup.find("input", {"id" : "fCreateDate"})
	date 	= 	date.get('value')
	date 	= 	strip_tags(date)
	date 	= 	clear_character_junk(date)
	if date == now:
		article_instance = [title, date, content]

		kcna_article = state_media_article(
			name = title,
			text = content,
			date = date,
			language = 'EN',
			)
		kcna_article.save()
		publication_object = state_media_publication.objects.get(name="KCNA")
		kcna_article.publication = publication_object
		kcna_article.save()
	else:
		pass
