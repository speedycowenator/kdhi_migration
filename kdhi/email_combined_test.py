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
		author = ''
		for authr in authors:
			author = author + authr
		author = clear_character_junk(author)

		content = content[:content_length]
		text_raw = ''
		text_html = ''
		for lines in content:
			text_html += lines + " "
			text_raw = text_raw + lines
		text_html = clear_character_junk(text_html)
		text_raw = clear_character_junk(text_raw)
		title = clear_character_junk(title)
		date_short = date_year + '-' + shorten(date_month) + '-' + date_day
		article = [title, text_html]
		article_raw = [title, text_raw]
		article_list.append(article)
		article_raw_list.append(article_raw)
	except:
		pass

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
three_pages	= ['One', 'Two']#, 'Three', 'Four', 'Five', 'Six']
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
	for a in soup.findAll('a'):
		del a['href']

	content = 	article_soup.find("input", {"id" : "content"})
	content = 	content.get('value')
	content =  	strip_tags(content)
	content = 	clear_character_junk(content)
	content = content.split("-- ")
	content = content[1]
	content = 	content.split("(")
	content_first = 	content[0]
	content_second = 	content[1]
	content_second = 	content_second.split(")")
	content_third  = 	content_second[1]
	content_second = 	content_second[0] 
	content = 	content_first +"(Link in original article removed for safety)" + content_third
	title 	= 	article_soup.find("input", {"id" : "mainTitle"})
	title 	= 	title.get('value')
	title 	= 	strip_tags(title)
	title 	= 	clear_character_junk(title)
	date 	= 	article_soup.find("input", {"id" : "fCreateDate"})
	date 	= 	date.get('value')
	date 	= 	strip_tags(date)
	date 	= 	clear_character_junk(date)
#	if date == now:
	article_instance = [title, date, content]
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
	a {font-family: "Open Sans", sans-serif; font-size: 0px; line-height: 0px; text-align: center; margin-top: 25px;  text-decoration: none;}
	a:visited {font-family: "Open Sans", sans-serif; font-size: 0px; line-height: 0px; text-align: center; margin-top: 25px; text-decoration: none;}
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

for article in article_list:
	article_strings = '<h5>'
	article_strings = article_strings + article[0]
	article_strings = article_strings + '</h5>'
	article_strings = article_strings + article[1]
	body_list.append(article_strings)
for formatted_article in body_list:
	for item in formatted_article:
		html += item
email_content = html
body_list_kcna = ["<h6> KCNA Articles </h6>"]

for article_kcna in kcna_article_list:
	article_strings = '<h5>'
	article_strings = article_strings + article_kcna[0]
	article_strings = article_strings + '</h5>'
	article_strings = article_strings + article_kcna[1] + "<br>"
	article_strings = article_strings + article_kcna[2]
	body_list_kcna.append(article_strings)
for formatted_article in body_list_kcna:
	for item in formatted_article:
		email_content += item

email_content += html_end

import smtplib
import email.message
gmail_user = 'kdhinews@gmail.com'
gmail_password = 'i@co%FvR83w2'


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