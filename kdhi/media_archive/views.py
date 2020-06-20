from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from datetime import date
import datetime
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import time
from datetime import date, timedelta
now = date.today()
import re
from django.utils.html import strip_tags
import bs4
import urllib.request

from media_archive.models import state_media_publication, state_media_author, state_media_article

url = 'https://kdhi.webflow.io/'

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find('link')
webflow_page_data = "5eb9f7c0c3ca3dae2a5b7301"

link_text = (link.get('href'))

def article_detail(request, pk):
	article_focused 	= state_media_article.objects.get(pk=pk)
    
	context = {
		'article_focused' 	: article_focused,
		'style_sheet'       : link_text,
		'webflow_page_data' : webflow_page_data,

	}
	return render(request, 'archive_pages/article_detail.html', context)
