
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from documents.models import document, document_collection, collection_timeline_item
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
    collection_name = document_detail.collection.name
    if collection_name == "The June Struggle":
    	collection_name = 'Democratization'
    url = 'https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Documents/' + collection_name + '/' + document_detail.slug +'.pdf'
    
    context = {
    		'url' 					: url,
            'document_detail'       : document_detail,
            'style_sheet'           : link_text,
            }
    return render(request, 'document_detail.html', context)

def collection_page(request, name):
	collection_set = []
	request_collection = document_collection.objects.get(name=name)
	request_pk = request_collection.pk
	try:
		for e in document.objects.filter(collection=request_pk):
			collection_set.append(e)
	except:
		collection_set.append(document.objects.get(collection=request_pk))
	

	context = {
			'collection'  		: request_collection,	
			'collection_set'	: collection_set, 
			'style_sheet'		: link_text,
	}
	return render(request, 'collection_page.html', context)

def timeline(request, init_year, end_year):
	timeline_years = []
	timeline_items = []
	timeline_items_cleaned = []
	for year in range(init_year, end_year + 1):
		timeline_years.append(year)


	for timelime_year_items in timeline_years:
		for timeline_item in collection_timeline_item.objects.filter(year=timelime_year_items):
			timeline_items.append(timeline_item)



	for timeline_item in timeline_items:
		day_content = []
		try:
			if len(timeline_item.day_1_content) != 0:
				day_content.append([timeline_item.day_1, timeline_item.day_1_content])
		except:
			pass

		try:
			if len(timeline_item.day_2_content) != 0:
				day_content.append([timeline_item.day_2, timeline_item.day_2_content])
		except:
			pass

		try:
			if len(timeline_item.day_3_content) != 0:
				day_content.append([timeline_item.day_3, timeline_item.day_3_content])
		except:
			pass

		try:
			if len(timeline_item.day_4_content) != 0:
				day_content.append([timeline_item.day_4, timeline_item.day_4_content])
		except:
			pass

		try:
			if len(timeline_item.day_5_content) != 0:
				day_content.append([timeline_item.day_5, timeline_item.day_5_content])
		except:
			pass

		try:
			if len(timeline_item.day_6_content) != 0:
				day_content.append([timeline_item.day_6, timeline_item.day_6_content])
		except:
			pass

		try:
			if len(timeline_item.day_7_content) != 0:
				day_content.append([timeline_item.day_7, timeline_item.day_7_content])
		except:
			pass

		try:
			if len(timeline_item.day_8_content) != 0:
				day_content.append([timeline_item.day_8, timeline_item.day_8_content])
		except:
			pass

		try:
			if len(timeline_item.day_9_content) != 0:
				day_content.append([timeline_item.day_9, timeline_item.day_9_content])
		except:
			pass

		try:
			if len(timeline_item.day_10_content) != 0:
				day_content.append([timeline_item.day_10, timeline_item.day_10_content])
		except:
			pass

		try:
			if len(timeline_item.day_11_content) != 0:
				day_content.append([timeline_item.day_11, timeline_item.day_11_content])
		except:
			pass

		try:
			if len(timeline_item.day_12_content) != 0:
				day_content.append([timeline_item.day_12, timeline_item.day_12_content])
		except:
			pass

		try:
			if len(timeline_item.day_13_content) != 0:
				day_content.append([timeline_item.day_13, timeline_item.day_13_content])
		except:
			pass

		try:
			if len(timeline_item.day_8_content) != 0:
				day_content.append([timeline_item.day_8, timeline_item.day_1_content])
		except:
			pass
		timeline_items_cleaned.append([timeline_item.year, timeline_item.month, timeline_item.media_src, timeline_item.media_text, day_content])


	context = {
			'timeline_years'	: timeline_years,
			'timeline_items_cleaned'	: timeline_items_cleaned,
			'day_content' 				: day_content,
			'style_sheet'				: link_text,
	}
	return render(request, 'timeline_test.html', context)
	
def document_list(request, name):
	collection_set = []
	request_collection = document_collection.objects.get(name=name)
	request_pk = request_collection.pk
	try:
		for e in document.objects.filter(collection=request_pk):
			collection_set.append(e)
	except:
		collection_set.append(document.objects.get(collection=request_pk))
	

	context = {

			'collection'  		: request_collection,	
			'collection_set'	: collection_set, 
			'style_sheet'		: link_text,
	}
	return render(request, 'document_list.html', context)