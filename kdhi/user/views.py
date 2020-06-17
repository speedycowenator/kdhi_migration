
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
import datetime
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from user.models import subscriber


import bs4
import urllib.request

url = 'https://kdhi.webflow.io/'

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")	
link = soup.find('link')

link_text = (link.get('href'))

def form_test(request):


	context = {
		'style_sheet'           : link_text,
		}
	return render(request, 'form_test.html', context)


def email_signup(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")

		subscriber.objects.create(
			name=name, 
			email=email

			)

	context = {
		'style_sheet'           : link_text,
		}
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))