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
import bs4
import urllib.request

from documents.models import document
from main_site.models import glossary_item, institution, individual, rok_institution, rok_individual, article, position
from trackers.models import overseas_tracker, inter_korean_tracker

url = 'https://kdhi.webflow.io/'
#url = 'https://kdhi-archive-code-builder.webflow.io/institution-page'
webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find('link')
webflow_page_data = '5eb9f7c0c3ca3dae2a5b7301'
link_text = (link.get('href'))

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find_all('script')
link_count = len(link)
java_loc = link_count - 2
java_location = link[java_loc]
java_location = java_location.get('src')



checked 	= 'checked'
unchecked 	= ''

def search_console(request):
	document_no_result_toggle 				= ''
	inst_no_result_toggle 					= ''
	inter_no_result_toggle 					= ''
	overseas_no_result_toggle 				= ''
	bio_no_result_toggle 					= ''
	articles_no_result_toggle 				= ''
	glossary_no_result_toggle  				= ''
	search_models_cleaned 					= []
	overseas_tracker_toggle_check			= []
	overseas_tracker_toggle_check_results 	= []

	document_toggle_check					= []
	document_toggle_check_results 			= []

	article_toggle_check					= []
	article_toggle_check_results 			= []

	inter_tracker_toggle_check				= []
	inter_tracker_toggle_check_results 		= []

	individual_toggle_check					= []
	individual_toggle_check_results 		= []

	institution_toggle_check				= []
	institution_toggle_check_results 		= []	

	glossary_item_toggle_check				= []
	glossary_item_toggle_check_results 		= []


	if request.method == 'GET':
		search_text = ''
	if request.method == 'POST':
		counter = 5 #number of models possible to search
		search_text		= request.POST.get('search')
		
		#Get models to search
		overseas_tracker_toggle_check = request.POST.get('overseas_tracker_toggle')
		if overseas_tracker_toggle_check == 'True':
			overseas_tracker_toggle_check_results = []
			for object_itr in overseas_tracker.objects.filter(name__icontains=search_text):
				overseas_tracker_toggle_check_results.append(object_itr)
			overseas_tracker_toggle_check = 'checked'

		document_toggle_check = request.POST.get('document_toggle')
		if document_toggle_check == 'True':
			document_toggle_check_results = []
			for object_itr in document.objects.filter(name__icontains=search_text):
				document_toggle_check_results.append(object_itr)
			document_toggle_check = 'checked'

		article_toggle_check = request.POST.get('article_toggle')
		if article_toggle_check == 'True':
			article_toggle_check_results = []
			for object_itr in article.objects.filter(name__icontains=search_text):
				article_toggle_check_results.append(object_itr)
			article_toggle_check = 'checked'

		inter_tracker_toggle_check = request.POST.get('inter_tracker_toggle')
		if inter_tracker_toggle_check == 'True':
			inter_tracker_toggle_check_results = []
			for object_itr in inter_korean_tracker.objects.filter(name__icontains=search_text):
				inter_tracker_toggle_check_results.append(object_itr)
			inter_tracker_toggle_check = 'checked'

		individual_toggle_check = request.POST.get('individual_toggle')
		if individual_toggle_check == 'True':
			individual_toggle_check_results = []
			for object_itr in individual.objects.filter(name__icontains=search_text):
				individual_positions = []
				for individual_position in position.objects.filter(person=object_itr):
					institution_tag = individual_position.institution
					inst_url = institution_tag.get_absolute_url
					individual_position_pair = [individual_position.institution, individual_position.title, inst_url]
					individual_positions.append(individual_position_pair)
				individual_toggle_check_results.append([object_itr, individual_positions])
			individual_toggle_check = 'checked'

		institution_toggle_check = request.POST.get('institution_toggle')
		if institution_toggle_check == 'True':
			institution_toggle_check_results = []
			for object_itr in institution.objects.filter(name__icontains=search_text):
				institution_toggle_check_results.append(object_itr)
			institution_toggle_check = 'checked'

		glossary_item_toggle_check = request.POST.get('glossary_item_toggle')
		if glossary_item_toggle_check == 'True':
			glossary_item_toggle_check_results = []
			for object_itr in glossary_item.objects.filter(name__icontains=search_text):
				glossary_item_toggle_check_results.append(object_itr)
			glossary_item_toggle_check = 'checked'

		#check for results 
		try: 
			if len(inter_tracker_toggle_check_results) > 0:
				inter_no_result_toggle = ''
			else: 
				inter_no_result_toggle = 'toggle'
		except: 
			inter_no_result_toggle = 'toggle'

		try: 
			if len(overseas_tracker_toggle_check_results) > 0:
				overseas_no_result_toggle = ''
			else: 
				overseas_no_result_toggle = 'toggle'
		except: 
			overseas_no_result_toggle = 'toggle'

		try: 
			if len(individual_toggle_check_results) > 0:
				bio_no_result_toggle = ''
			else: 
				bio_no_result_toggle = 'toggle'
		except: 
			bio_no_result_toggle = 'toggle'

		try: 
			if len(article_toggle_check_results) > 0:
				articles_no_result_toggle = ''
			else: 
				articles_no_result_toggle = 'toggle'
		except: 
			articles_no_result_toggle = 'toggle'

		try: 
			if len(glossary_item_toggle_check_results) > 0:
				glossary_no_result_toggle = ''
			else: 
				glossary_no_result_toggle = 'toggle'
		except: 
			glossary_no_result_toggle = 'toggle'

		try: 
			if len(institution_toggle_check_results) > 0:
				inst_no_result_toggle = ''
			else: 
				inst_no_result_toggle = 'toggle'
		except: 
			inst_no_result_toggle = 'toggle'

		try: 
			if len(document_toggle_check_results) > 0:
				document_no_result_toggle = ''
			else: 
				document_no_result_toggle = 'toggle'
		except: 
			document_no_result_toggle = 'toggle'
	

	context = {
			'overseas_tracker_toggle_check' 		: overseas_tracker_toggle_check,
			'document_toggle_check' 				: document_toggle_check,
			'article_toggle_check' 					: article_toggle_check,
			'inter_tracker_toggle_check' 			: inter_tracker_toggle_check,
			'individual_toggle_check' 				: individual_toggle_check,
			'institution_toggle_check' 				: institution_toggle_check,
			'glossary_item_toggle_check' 			: glossary_item_toggle_check,
	        'search_text'							: search_text,
	        'style_sheet'           				: link_text,
	        'overseas_tracker_toggle_check_results' : overseas_tracker_toggle_check_results,
	        'document_toggle_check_results' 		: document_toggle_check_results, 
	        'article_toggle_check_results' 			: article_toggle_check_results,
	        'inter_tracker_toggle_check_results' 	: inter_tracker_toggle_check_results,
	        'individual_toggle_check_results' 		: individual_toggle_check_results,
	        'institution_toggle_check_results' 		: institution_toggle_check_results,
	        'glossary_item_toggle_check_results' 	: glossary_item_toggle_check_results,
	        'document_no_result_toggle' 			: document_no_result_toggle, 
	        'inst_no_result_toggle' 				: inst_no_result_toggle, 
	        'inter_no_result_toggle' 				: inter_no_result_toggle, 
	        'overseas_no_result_toggle' 			: overseas_no_result_toggle, 
	        'bio_no_result_toggle' 					: bio_no_result_toggle, 
	        'articles_no_result_toggle' 			: articles_no_result_toggle, 
	        'glossary_no_result_toggle' 			: glossary_no_result_toggle, 
	        'java_location'     : java_location,


	        }
	return render(request, 'search_console.html', context)

					
