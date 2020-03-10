import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from news_archive.models import article
import csv

with open('articles_import.csv', newline='', encoding='utf-8') as csvfile:
	article_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in article_reader:
		date_fixed = ''
		date = row[4]
		for character in date:
			if character == '/':
				character = '-'
			date_fixed += character
		date_fixed_list = date_fixed.split('-')
		date_fixed = date_fixed_list[2] + '-' + date_fixed_list[0] + '-' + date_fixed_list[1]

		date = date_fixed

		title = row[1]
		title= title.replace('*', ',')
		title= title.replace('^', '"')
		text = row[2]
		author = row[3]
		text= text.replace('**', ',')
		text= text.replace('^', '"')

		b = article(title=title, summary=text, date_publication=date, author=author)
		b.save()
		print(row[0])
		print(title)
		print(text)
		print(author)
		print(date)
		print('---------------------')



