
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from documents.models import document
from datetime import date
import datetime
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect




import bs4
import urllib.request

url = 'https://kdhi-archive-code-builder.webflow.io/event'

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find('link')


link_text = (link.get('href'))


def document_detail(request, slug):
    document_detail = document.objects.get(slug=slug)
    
    context = {
            'document_detail'       : document_detail,
            'style_sheet'           : link_text,
            }
    return render(request, 'document_detail.html', context)



