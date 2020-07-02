import time
from datetime import date
import datetime
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import strip_tags
import bs4
from media_archive.models import state_media_publication, state_media_author, state_media_article, uritv_video
import urllib.request
from django.db.models import Q
last_week = timezone.now().date() - timedelta(days=7)

url = 'https://kdhi.webflow.io/'

time_options = {
			"week" : timezone.now().date() - timedelta(days=7),
			"month" : timezone.now().date() - timedelta(days=30),
			"year" : timezone.now().date() - timedelta(days=365),
			"twelve_years" : timezone.now().date() - timedelta(days=4380),
			"all" : timezone.now().date() - timedelta(days=17885),
		}

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find('link')
webflow_page_data = "5eb9f7c0c3ca3dae2a5b7301"
link_text = (link.get('href'))

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find_all('script')
link_count = len(link)
java_loc = link_count - 2
java_location = link[java_loc]
java_location = java_location.get('src')

def article_detail(request, pk):
	article_focused 	= state_media_article.objects.get(pk=pk)
    
	context = {
		'java_location' 	: java_location,
		'article_focused' 	: article_focused,
		'style_sheet'       : link_text,
		'webflow_page_data' : webflow_page_data,

	}
	return render(request, 'archive_pages/article_detail.html', context)

def video_archive_detail(request, pk):
	video_detail = uritv_video.objects.get(pk=pk)
	link_sourcetype = video_detail.get_sourcetype()
	link_sourcetype = link_sourcetype[0]
	if link_sourcetype == "centertv":
		link_sourcetype = "ccentv"
	uri_link = "http://www.uriminzokkiri.com/index.php?ptype={}&mtype=view&no={}#pos".format(link_sourcetype, video_detail.db_code)
	webflow_page_data = "5ef37ce11288cb0144e73820"

	context = {
		'video_detail' 		: video_detail,
		'uri_link' 			: uri_link,
		'java_location' 	: java_location,
		'style_sheet'       : link_text,
		'webflow_page_data' : webflow_page_data,
	}
	return render(request, 'archive_pages/uritv_video.html', context)


def video_archive_list(request):
	video_list = uritv_video.objects.filter(db_code__lte=36100)
	context = {
		'video_list' 		: video_list,
		'java_location' 	: java_location,
		'style_sheet'       : link_text,
		'webflow_page_data' : webflow_page_data,
	}
	return render(request, 'archive_pages/video_archive_list.html', context)

def article_list(request):
	search_type_checked_both = 'checked=""'
	search_type_checked_text = ''
	search_type_checked_title = ''
	time_checked_week = 'checked=""'
	time_checked_month = ''
	time_checked_year = ''
	time_checked_twelve = ''
	time_checked_all = ''
	publication = 'all'
	time_frame = 'week'
	if request.method == 'GET':
		#'last_week' variable set in header section
		#Function returns list of articles in last week so search page isn't empty
		time_frame_key = time_options["week"]
		search_text = ''
		search_type = 'both'
		article_list = state_media_article.objects.filter(date__gt=time_frame_key).all()

	elif request.method == 'POST':

		search_type = request.POST.get("search_type_selection_field")
		search_text = request.POST.get("search_text")
		#Selecting search type
		if search_type == 'both':
			article_list = state_media_article.objects.filter(
				Q(name__icontains=search_text) | Q(text__icontains=search_text)
				)
		elif search_type == 'title':
			search_type_checked_both = ''
			search_type_checked_title = 'checked=""'
			article_list = state_media_article.objects.filter(name__icontains=search_text)

		elif search_type == 'text':
			article_list = state_media_article.objects.filter(text__icontains=search_text)
			search_type_checked_both = ''
			search_type_checked_text = 'checked=""'


		time_frame 		= request.POST.get("time_frame")
		time_frame_key = time_options[time_frame]
		article_list = article_list.filter(date__gt=time_frame_key)



		if time_frame == 'month':
			time_checked_month = 'checked=""'
			time_checked_week = ''

		if time_frame == 'year':
			time_checked_year = 'checked=""'
			time_checked_week = ''

		if time_frame == 'twelve_years':
			time_checked_twelve = 'checked=""'
			time_checked_week = ''

		if time_frame == 'all':
			time_checked_all = 'checked=""'
			time_checked_week = ''

		publication 	= request.POST.get("publication")
		if publication == "KCNA":
			article_list = article_list.filter(publication__name=publication)
		elif publication == "RS":
			article_list = article_list.filter(publication__name=publication)

		sort_direction 	= request.POST.get("sort_direction")
		sort_method 	= request.POST.get("sort_method")
		sort_function = sort_direction + sort_method
		article_list = article_list.order_by(sort_function)



		
	context = {
		'publication' : publication,
		'time_frame' : time_frame,
		'time_checked_week': time_checked_week,
		'time_checked_month' : time_checked_month,
		'time_checked_year' : time_checked_year,
		'time_checked_twelve' : time_checked_twelve,
		'time_checked_all' : time_checked_all,
		'search_type_checked_both' : search_type_checked_both,
		'search_type_checked_text' : search_type_checked_text,
		'search_type_checked_title' : search_type_checked_title,
		'search_type' 		: search_type,
		'search_text' 		: search_text, 	
		'article_list' 		: article_list,
		'java_location' 	: java_location,
		'style_sheet'       : link_text,
		'webflow_page_data' : webflow_page_data,
	}
	return render(request, 'archive_pages/article_list.html', context)
'''
time_frame
publication
sort_direction
sort_method
'''