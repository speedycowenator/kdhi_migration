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
from index_test.models import face_instance, individual_instance

url = 'https://kuroko-template.webflow.io/old-home'

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find('link')


link_text = (link.get('href'))

def figure_page(request, id):
	figure_page_iter = individual_instance.objects.get(pk=id)

    context = {
        'style_sheet'       : link_text,

    }
    return render(request, 'figure_page.html', context)

def face_page(request, kuroko_id):
    context = {
        'style_sheet'       : link_text,

    }
    return render(request, 'face_page.html', context)
