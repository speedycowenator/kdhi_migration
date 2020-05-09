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

from main_site.models import glossary_item, individual, glossary_item, institution, position, rok_individual, rok_institution, rok_individual, rok_position, article
from documents.models import document, document_collection, collection_timeline_item, critical_oral_history
from trackers.models import overseas_tracker, inter_korean_tracker, overseas_topic, country_list

url = 'https://kdhi-archive-code-builder.webflow.io/event'

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find('link')
link_text = (link.get('href'))

checked 	= 'checked'
unchecked 	= ''

def search_console(request):
	search_models_cleaned = []
	search_model_1_check 	= unchecked
	search_model_2_check 	= unchecked
	search_model_3_check 	= unchecked
	search_model_4_check 	= unchecked
	search_model_5_check 	= unchecked
	search_model_6_check 	= unchecked

	if request.method == 'GET':
		search_text = "Enter your search here."		
	if request.method == 'POST':
		counter = 5 #number of models possible to search
		search_text		= request.POST.get('search')
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

		search_model_6_data = request.POST.get('search_model_6')
		try: 
			if len(search_model_6_data) != 0:
				search_models_cleaned.append(search_model_6_data)	
				search_model_6_check 	= checked
		except:
			search_model_6_check 	= unchecked



	


	context = {
			'search_model_1_check' 	: search_model_1_check,
			'search_model_2_check' 	: search_model_2_check,
			'search_model_3_check' 	: search_model_3_check,
			'search_model_4_check' 	: search_model_4_check,
			'search_model_5_check' 	: search_model_5_check,
			'search_model_6_check' 	: search_model_6_check,
			'search_model' 			: search_models_cleaned,
	        'search_text'			: search_text,
	        'style_sheet'           : link_text,
	        }
	return render(request, 'search_console.html', context)

