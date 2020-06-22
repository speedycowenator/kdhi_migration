
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from documents.models import document, document_collection, collection_timeline_item, critical_oral_history, document_keyword
from datetime import date
import datetime
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect




import bs4
import urllib.request

url = 'https://kdhi.webflow.io/'

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find('link')

democratization_proxy = "1987 Democratization Movement"
link_text = (link.get('href'))

checked 	= 'checked'
unchecked 	= ''


def document_detail(request, slug):
	document_detail = document.objects.get(slug=slug)
	collection_inst = document_detail.collection
	collection_inst_name = collection_inst.name
	collection_inst_dir = collection_inst.directory

	if collection_inst_name == democratization_proxy:
		collection_name = 'Democratization'
	url = collection_inst_dir  + document_detail.slug +'.pdf'

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

def timeline_chrono(request, init_year, end_year):
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
	#if name == democratization_proxy:
	#	name = 'Democratization'
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

def korean_democratization_project_landing(request):

	#
	#
	#

	context = {
	    'style_sheet'           : link_text,

	}

	return render(request, 'korean_democratization_page.html', context)


def documents_landing(request):
	collection_cards 	= document_collection.objects.all()
	collection_card_set = []
	card_counter 		= 0 
	for collection_card in collection_cards:
		if card_counter == 0:
			featured_card = collection_card
		elif card_counter <=4:
			if document.objects.filter(collection=collection_card).count() != 0:
				card_planned_check = ""
			else: 
				card_planned_check = "Collection Coming Soon"	
			collection_card_set.append([collection_card, card_planned_check])
		else:
			pass
		card_counter += 1
	document_list_cleaned 	= []
	search_models_cleaned 	= []
	start_date				= []
	end_date 				= []
	search_model_1_check 	= unchecked
	search_model_2_check 	= unchecked
	search_model_3_check 	= unchecked
	search_model_4_check 	= unchecked
	search_model_5_check 	= unchecked
	search_model_6_check 	= unchecked
	document_list = []	
	keyword_selection = []

	keyword_list 	= request.POST.getlist('keyword-selection')
	keyword_selection_raw = document_keyword.objects.all()

	for keyword in keyword_selection_raw:
		if keyword.name in keyword_list:
			selection_item = '''<option selected="selected" value="{}">{}</option>'''.format(keyword.name, keyword.name)
		else: 
			selection_item = '''<option value="{}">{}</option>'''.format(keyword.name, keyword.name)
		keyword_selection.append(selection_item)

	if request.method == 'GET':
		search_text = ''
	if request.method == 'POST':
		counter = 5 #number of models possible to search
		search_text		= request.POST.get('text-search')
		search_model_fields 	= ['search_model_1_data', 'search_model_2', 'search_model_3', 'search_model_4', 'search_model_5' ,'search_model_6']
		
		search_model_1_data = request.POST.get('search_model_1')
		try: 
			if len(search_model_1_data) != 0:
				search_models_cleaned.append(search_model_1_data)	
				search_model_1_check 	= checked
		except:
			search_model_1_check 	= unchecked

		search_model_2_data = request.POST.get('search_model_2')
		try: 
			if len(search_model_2_data) != 0:
				search_models_cleaned.append(search_model_2_data)	
				search_model_2_check 	= checked
		except:
			search_model_2_check 	= unchecked

		search_model_3_data = request.POST.get('search_model_3')
		try: 
			if len(search_model_3_data) != 0:
				search_models_cleaned.append(search_model_3_data)	
				search_model_3_check 	= checked
		except:
			search_model_3_check 	= unchecked

		search_model_4_data = request.POST.get('search_model_4')
		try: 
			if len(search_model_4_data) != 0:
				search_models_cleaned.append(search_model_4_data)	
				search_model_4_check 	= checked
		except:
			search_model_4_check 	= unchecked

		search_model_5_data = request.POST.get('search_model_5')
		try: 
			if len(search_model_5_data) != 0:
				search_models_cleaned.append(search_model_5_data)	
				search_model_5_check 	= checked
		except:
			search_model_5_check 	= unchecked

		start_date 		= request.POST.get('date-search-start')
		end_date 		= request.POST.get('date-search-end')
		for collection in search_models_cleaned:
			if len(keyword_list) > 0:
				for keyword_itt in keyword_list:
					for doc in document.objects.filter(name__icontains=search_text, collection__name=collection, keywords__name=keyword_itt, date__gte=start_date, date__lte=end_date):
						document_list.append(doc)
		document_list_cleaned = list(dict.fromkeys(document_list))

	context = {
			'search_model_1_check' 	: search_model_1_check,
			'search_model_2_check' 	: search_model_2_check,
			'search_model_3_check' 	: search_model_3_check,
			'search_model_4_check' 	: search_model_4_check,
			'search_model_5_check' 	: search_model_5_check,
			'search_model' 			: search_models_cleaned,
			'search_text'			: search_text,
			'style_sheet'           : link_text,
			'document_list' 		: document_list_cleaned,
			'keyword_selection'		: keyword_selection,
			'start_date' 			: start_date,
			'end_date' 				: end_date,
			'keyword_list'			: keyword_list,
			'start_date' 			: start_date,
			'end_date' 				: end_date,
			'featured_card' 		: featured_card,
			'collection_card_set' 	: collection_card_set
			}

	return render(request, 'document_collection_landing.html', context)


def timelines_landing(request):
	collection_cards 	= document_collection.objects.all()
	collection_card_set = []
	card_counter 		= 0 
	for collection_card in collection_cards:
		if card_counter == 0:
			featured_card = collection_card
		elif card_counter <=4:
			if document.objects.filter(collection=collection_card).count() != 0:
				card_planned_check = ""
			else: 
				card_planned_check = "Collection Coming Soon"	
			collection_card_set.append([collection_card, card_planned_check])
		else:
			pass
		card_counter += 1



	context = {
	    'style_sheet'           : link_text,
	    'featured_card' 		: featured_card,
	    'collection_card_set' 	: collection_card_set

	}

	return render(request, 'timeline_collection_landing.html', context)




def collection_timeline(request, name):
		#need to add in a way to recognize other timeline items, ideally by fixing the 'models not loaded' bug or transitioning to foreign key
	timeline_items_cleaned = []
	if name == democratization_proxy:
		name = 'democratization'
		timeline_set = collection_timeline_item.objects.filter(section_title__icontains=name).all()
		collection_header = democratization_proxy
	else:
		timeline_set = collection_timeline_item.objects.filter(collection__name=name).all()
		collection_header = name
	for timeline_item in timeline_set:
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
			'timeline_items_cleaned'	: timeline_items_cleaned,
			'style_sheet'				: link_text,
			'collection_header' 		: collection_header,
	}
	return render(request, 'timeline_test.html', context)


def critical_oral_history_detail(request, session):
	coh_item = critical_oral_history.objects.get(session=session)


	context = {
			'coh_item'		: coh_item,
			'style_sheet'	: link_text,
	}
	return render(request, 'critical_oral_history_detail.html', context)



def critical_oral_history_landing(request):
	collection_cards 	= critical_oral_history.objects.all()
	collection_card_set = []
	card_counter 		= 0 
	for collection_card in collection_cards:
		if card_counter == 0:
			featured_card = collection_card
		elif card_counter <=4:
			if document.objects.filter(collection=collection_card).count() != 0:
				card_planned_check = ""
			else: 
				card_planned_check = "Collection Coming Soon"	
			collection_card_set.append([collection_card, card_planned_check])
		else:
			pass
		card_counter += 1
		
	context = {
	    'style_sheet'           : link_text,
	    'featured_card' 		: featured_card,
	    'collection_card_set' 	: collection_card_set

	}

	return render(request, 'critical_oral_history_landing.html', context)



def document_search(request):
	document_list_cleaned 	= []
	search_models_cleaned 	= []
	start_date				= []
	end_date 				= []
	search_model_1_check 	= unchecked
	search_model_2_check 	= unchecked
	search_model_3_check 	= unchecked
	search_model_4_check 	= unchecked
	search_model_5_check 	= unchecked
	search_model_6_check 	= unchecked
	document_list = []	
	keyword_selection = []

	keyword_list 	= request.POST.getlist('keyword-selection')
	keyword_selection_raw = document_keyword.objects.all()

	for keyword in keyword_selection_raw:
		if keyword.name in keyword_list:
			selection_item = '''<option selected="selected" value="{}">{}</option>'''.format(keyword.name, keyword.name)
		else: 
			selection_item = '''<option value="{}">{}</option>'''.format(keyword.name, keyword.name)
		keyword_selection.append(selection_item)

	if request.method == 'GET':
		search_text = ''
	if request.method == 'POST':
		counter = 5 #number of models possible to search
		search_text		= request.POST.get('text-search')
		search_model_fields 	= ['search_model_1_data', 'search_model_2', 'search_model_3', 'search_model_4', 'search_model_5' ,'search_model_6']
		
		search_model_1_data = request.POST.get('search_model_1')
		try: 
			if len(search_model_1_data) != 0:
				search_models_cleaned.append(search_model_1_data)	
				search_model_1_check 	= checked
		except:
			search_model_1_check 	= unchecked

		search_model_2_data = request.POST.get('search_model_2')
		try: 
			if len(search_model_2_data) != 0:
				search_models_cleaned.append(search_model_2_data)	
				search_model_2_check 	= checked
		except:
			search_model_2_check 	= unchecked

		search_model_3_data = request.POST.get('search_model_3')
		try: 
			if len(search_model_3_data) != 0:
				search_models_cleaned.append(search_model_3_data)	
				search_model_3_check 	= checked
		except:
			search_model_3_check 	= unchecked

		search_model_4_data = request.POST.get('search_model_4')
		try: 
			if len(search_model_4_data) != 0:
				search_models_cleaned.append(search_model_4_data)	
				search_model_4_check 	= checked
		except:
			search_model_4_check 	= unchecked

		search_model_5_data = request.POST.get('search_model_5')
		try: 
			if len(search_model_5_data) != 0:
				search_models_cleaned.append(search_model_5_data)	
				search_model_5_check 	= checked
		except:
			search_model_5_check 	= unchecked

		start_date 		= request.POST.get('date-search-start')
		end_date 		= request.POST.get('date-search-end')
		for collection in search_models_cleaned:
			if len(keyword_list) > 0:
				for keyword_itt in keyword_list:
					for doc in document.objects.filter(name__icontains=search_text, collection__name=collection, keywords__name=keyword_itt, date__gte=start_date, date__lte=end_date):
						document_list.append(doc)
		document_list_cleaned = list(dict.fromkeys(document_list))

	context = {
			'search_model_1_check' 	: search_model_1_check,
			'search_model_2_check' 	: search_model_2_check,
			'search_model_3_check' 	: search_model_3_check,
			'search_model_4_check' 	: search_model_4_check,
			'search_model_5_check' 	: search_model_5_check,
			'search_model' 			: search_models_cleaned,
			'search_text'			: search_text,
			'style_sheet'           : link_text,
			'document_list' 		: document_list_cleaned,
			'keyword_selection'		: keyword_selection,
			'start_date' 			: start_date,
			'end_date' 				: end_date,
			'keyword_list'			: keyword_list,
			'start_date' 			: start_date,
			'end_date' 				: end_date,
			}
	return render(request, 'document_search.html', context)



