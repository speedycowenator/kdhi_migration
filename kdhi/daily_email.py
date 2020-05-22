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
from django.utils.html import strip_tags
import os



now = (date.fromtimestamp(time.time()))
now = now.strftime('%Y-%m-%d')

now_subject = (datetime.datetime.now())
now_subject = now_subject.strftime('%m-%d')

def lengthen(date):
	return (month_dictionary_long[date])
def shorten(date):
	return (month_dictionary_short[date])

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
	line     = line.replace('\ufe16', '?')
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

seed(time.time())
seed(time.time())

proxies = {
	'http': 'socks5://x0506967:h9JWhEtghn@proxy-nl.privateinternetaccess.com:1080',
	'https': 'socks5://x0506967:h9JWhEtghn@proxy-nl.privateinternetaccess.com:1080',

	}

now = (date.fromtimestamp(time.time()))
now = now.strftime('%Y-%m-%d')

URL = 'http://kcna.kp/kcna.user.article.retrieveArticleInfoFromArticleCode.kcmsf'

LANGUAGE = 'eng'
kwContent = '' #appears to be an unused variable in KCNA database, always lists as a blank value

URL_LIST = 'http://kcna.kp/http://kcna.kp/kcna.user.article.retrieveNewsViewInfoList.kcmsf'
page_start = ['0']
kwDispTitle = ''
keyword = ''
newsTypeCode = 'NT41'
articleTypeList = ''
photoCount = '0'
movieCount = '0'
kwDispTitle = ''
kwContent = '' #appears to be an unused variable in KCNA database, always lists as a blank value
fromDate = ''
toDate = ''
LANGUAGE = 'eng'
codes_cleaned = []


#--------    FUNCTIONS   -----------------
def refresh_IP():
	initial_ip = (requests.get('http://ip.42.pl/raw', proxies=proxies).text)
	print(initial_ip)
	try:
		time.sleep(2)
		reset_test = True
		while reset_test == True:
			try:
				time.sleep(2)
				test_ip = requests.get('http://ip.42.pl/raw', proxies=proxies).text
				reset_test = test_ip==initial_ip
			except:
				time.sleep(2)
			print("Waiting for reset")
	except:
		time.sleep(2)
		test_ip = requests.get('http://ip.42.pl/raw', proxies=proxies).text
		reset_test = test_ip==initial_ip
	pass

article_list_kcna = []

#----------------------------------------------------------------
article_list_kcna = []
#----------------------------------------------------------------
print()
print("Initiating KCNA Phase")

#----------------------------------------------------------------
print()
print("Initiating Article Code Collection")
itteration = 0

for pages in page_start:
	initial_ip = (requests.get('http://ip.42.pl/raw', proxies=proxies).text)
	reset_test = True

	print()
	print("Processing articles on Page " + str(itteration))
	print("Operating under IP: " + initial_ip)
	print()
	itteration +=10
	DATA_LIST = {'page_start' : pages,
		'kwDispTitle' : kwDispTitle,
		'keyword' : keyword,
		'newsTypeCode' : newsTypeCode,
		'articleTypeList' : articleTypeList,
		'photoCount' : photoCount,
		'movieCount' : movieCount,
		'kwDispTitle' : kwDispTitle,
		'kwContent' : kwContent,
		'fromDate' : fromDate,
		'toDate' : toDate,
		'lang' : ''
		}
	news_pull = requests.post(url = URL_LIST, data = DATA_LIST, proxies=proxies)

	codes = news_pull.text
	codes = codes.split('dispTitle')
	codes = codes[0]
	codes = codes.split('<articleCode>')
	codes = codes[1:]

	fuzz_char_codes = ['<', '!', '[', 'CDATA', ']', '>', '/', '-0-', '\r', '\n']
	for code in codes:
		code = code.replace('</articleCode>', '')
		for char in fuzz_char_codes:
			code = code.replace(char, '')
		codes_cleaned.append(code)
	print("Step complete")
	print()
print("codes: codes")
print("Code collection finished")

#----------------------------------------------------------------

print()
print("Initiating article collection")
for ARs in codes_cleaned:
	print("Processing article " + ARs)
	print("Operating under IP: " + initial_ip)
	print()

	DATA = {'lang' : LANGUAGE,
			'kwContent' : kwContent,
			'article_code' : ARs
			}

	news_pull = requests.post(url = URL, data = DATA, proxies=proxies)

	full_response = news_pull.text

	title = full_response.split('dispTitle>')
	title = title[1]
	title_stripped = strip_tags(title)
	if len(title_stripped) ==0:
		title = title_stripped

	fuzz_char = ['nobrstrongfont', 'style=', 'font-size:11pt;', '<br>', '<', '!', '[', 'CDATA', ']', '>', '/', '-0-']

	for char in fuzz_char:
		title = title.replace(char, '')

	body_text = full_response.split('content')
	body_text = body_text[1]
	body_text = body_text.split('[')[2]
	body_text = body_text.split(']')[0]
	body_text = strip_tags(body_text)
	body_text = clear_character_junk(body_text)

	date = full_response.split('newsCreatedDate')
	date = date[1]
	for char in fuzz_char:
		date = date.replace(char, '')
	date = date.replace('.', '-')
	article = [title, body_text]
	print(article[0])
	print("Step complete")
	print()
