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

email_content = "TEST"


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
