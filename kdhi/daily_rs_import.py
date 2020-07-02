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

url_range_root= 'http://www.rodong.rep.kp/en/index.php?strPageID=SF01_02_01&newsID=' + now + '-'
url_stem_range = ['0001', '0002','0003', '0004', '0005', '0006', '0007', '0008', '0009', '0010', '0011', '0012', '0013', '0014', '0015', '0016', '0017', '0018', '0019']
url_library = []
article_raw_list = []

article_string = ''
article_list = []
for urls in url_stem_range:
	url = url_range_root + urls
	url_library.append(url)

month_dictionary_long  = {
			'Jan': 'January',
			'Feb': 'February',
			'Mar': 'March',
			'Apr': 'April',
			'May': 'May',
			'Jun': 'June',
			'Jul': 'July',
			'Aug': 'August',
			'Sep': 'September',
			'Oct': 'October',
			'Nov': 'November',
			'Dec': 'December',
			}
month_dictionary_short  = {
			'Jan': '01',
			'Feb': '02',
			'Mar': '03',
			'Apr': '04',
			'May': '05',
			'Jun': '06',
			'Jul': '07',
			'Aug': '08',
			'Sep': '09',
			'Oct': '10',
			'Nov': '11',
			'Dec': '12',
			}

def lengthen(date):
	return (month_dictionary_long[date])
def shorten(date):
	return (month_dictionary_short[date])

for url_itteration in url_library:
	try:
		link = url_itteration
		webpage=str(urllib.request.urlopen(link).read())
		soup_dirty = bs4.BeautifulSoup(webpage, features = "lxml")
		soup = soup_dirty
		mass_text = soup.prettify()
		mass_text = strip_tags(mass_text)
		date_month	= soup.find("div", class_="ArticleMenuContainer").get_text()
		date_month	= date_month.replace('.', '.')
		date_month	= date_month.split('.')[0]
		date_day	= soup.find("div", class_="ArticleMenuContainer").get_text()
		date_day.replace('.', '.')
		date_day	= date_day.split(',')[0]
		date_day	= date_day.split('.')[1]
		date_year	= soup.find("div", class_="ArticleMenuContainer").get_text()
		date_year	= date_year.split('(')[1]
		date_DOTW	= date_year.split(')')[1]
		date_year	= date_year.split(')')[0]
		len_month = len(date_month)
		len_snip = len_month - 3
		date_month = date_month[len_snip:]
		date_year	= clear_character_junk(date_year)
		date_day	= clear_character_junk(date_day)
		date_day = date_day.replace(' ', '')
		if len(date_day) != 2:
			date_day = '0' + date_day
		date_DOTW	= clear_character_junk(date_DOTW)
		date_month	= clear_character_junk(date_month)
		title = soup.find('p', class_="ArticleContent").get_text()
		content = []
		for line in soup.find_all('p', class_="ArticleContent"):
			content.append(line.get_text())
		content = content[2:]
		content_length = len(content) - 1
		authors = content[content_length:]
		try: 
			author = clear_character_junk(authors)
		except:
			author = ''
		content = content[:content_length]
		text_raw = ''
		text_html = ''
		for lines in content:
			text_html += lines + " "
			text_raw = text_raw + lines
		text_html = clear_character_junk(text_html)
		text_raw = clear_character_junk(text_raw)
		text_raw = text_raw.replace('.', '. ')
		title = clear_character_junk(title)
		date_short = date_year + '-' + shorten(date_month) + '-' + date_day
		article = [title, text_html]
		rodong_article = [title, text_raw, date_short, author]
		article_list.append(rodong_article)

		rodong_article = state_media_article(
			name = title,
			author = author,
			text = text_raw,
			date = date_short,
			language = 'EN',
			)
		rodong_article.save()
		publication_object = state_media_publication.objects.get(name="Rodong Sinmun")
		rodong_article.publication = publication_object
		rodong_article.save()
	except:
		pass
