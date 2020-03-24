
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from main_site.models import individual, glossary_item, institution, position, rok_individual, rok_institution, rok_individual, rok_position, article
from documents.models import document_collection
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

import bs4
import urllib.request

url = 'https://kdhi-archive-code-builder.webflow.io/event'

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find('link')


link_text = (link.get('href'))

def glossary_detail(request, slug):
    glossary_item = glossary_item.get(slug=slug)

    context = {
        'glossary_item'     : glossary_item,
        'style_sheet'       : link_text,

    }
    return render(request, 'glossary_detail.html', context)


def article_detail(request, slug):
    article_ref = article.objects.get(slug=slug)



    context = {
        'style_sheet'           : link_text,
        'article'   : article_ref,
        }
        
    return render(request, 'article_detail.html', context)


def homepage_view(request):

    collection_feature      = document_collection.objects.get(name="Democratization")
    collection_feature_url  = collection_feature.get_absolute_url
    latest_article          = article.objects.latest('update_date')

    secondary_article_list_full  = []
    counter                 = 0
    for article_temp in article.objects.all():
        secondary_article_list_full.append(article_temp)
    secondary_article_list = secondary_article_list_full[1:3]


    context = {
        'style_sheet'               : link_text,
        'collection_feature'        : collection_feature,
        'latest_article'            : latest_article,
        'secondary_article_list'    : secondary_article_list,

    }
    
    return render(request, 'static_pages/homepage.html', context)

def individual_detail(request, name):
    individual_detail = individual.objects.get(name=name)
    individual_positions = []
    for individual_position in position.objects.filter(person=individual_detail):
        institution_tag = individual_position.institution
        inst_url = institution_tag.get_absolute_url
        individual_position_pair = [individual_position.institution, individual_position.title, inst_url]
        individual_positions.append(individual_position_pair)
    
    context = {
            'individual_name'       : individual_detail.name,
            'individual_photo'      : individual_detail.full_resolution_photo,
            'individual_birthday'   : individual_detail.birthday,
            'individual_education'  : individual_detail.education,
            'individual_biography'  : individual_detail.bio,
            'individual_sources'    : individual_detail.sources,
            'individual_hometown'   : individual_detail.hometown,
            'individual_positions'  : individual_positions,
            'style_sheet'             : link_text,
            
            }
    return render(request, 'biographic_page.html', context)


def institution_detail(request, name):
    institution_detail  = institution.objects.get(name=name)
    inst_members            = []    #get all people with positions at insitution 
    member_titles           = []    #get titles for all members (duplicates)
    unique_titles           = []    #get all unique titles 
    grouped_members         = []    #group members by title (needs to nestled within title indent)
    inst_member_dic         = []    #list with double sublist where first item in first sublist is title and second item is a second list of all names with that title
    grouped_members_temp    = []
    
    
    #find all members
    
    
    for members in position.objects.filter(institution=institution_detail):
        member_tag = members.person
        member_url = member_tag.get_absolute_url
        for e in position.objects.filter(institution=institution_detail, person=member_tag):
            member_title = e.title 
            if member_title not in unique_titles:
                unique_titles.append(member_title)
    for title in unique_titles:
        grouped_members_temp = []
        for title_holder in position.objects.filter(institution=institution_detail, title=title):
            title_holder = title_holder.person
            title_holder_name = title_holder.name
            title_holder_url = title_holder.get_absolute_url
            title_holder_photo = title_holder.full_resolution_photo
            grouped_members_temp.append([title_holder_name, title_holder_url, title_holder_photo])
        grouped_members = [title, grouped_members_temp]
        inst_member_dic.append(grouped_members)
    
    
    context = {
            
            'institution_name'      : institution_detail.name,
            'institution_korean'    : institution_detail.name_korean,
            'institution_function'  : institution_detail.function,
            'institution_add'       : institution_detail.additional_information,
            'inst_member_dic'       : inst_member_dic,
            'style_sheet'             : link_text,
            }
    
    
    return render(request, 'institution_page.html', context)


def rok_individual_detail(request, name):
    individual_detail = rok_individual.objects.get(name=name)
    individual_positions = []
    for individual_position in rok_position.objects.filter(person=individual_detail):
        institution_tag = individual_position.institution
        inst_url = institution_tag.get_absolute_url
        individual_position_pair = [individual_position.institution, individual_position.title, inst_url]
        individual_positions.append(individual_position_pair)
    
    context = {
            'individual_name'       : individual_detail.name,
            'individual_photo'      : individual_detail.full_resolution_photo,
            'individual_sources'    : individual_detail.sources,
            'individual_positions'  : individual_positions,
            'style_sheet'             : link_text,           
            }
    return render(request, 'biographic_page.html', context)
def rok_institution_detail(request, name):
    institution_detail      = rok_institution.objects.get(name=name)
    inst_members            = []    #get all people with positions at insitution 
    member_titles           = []    #get titles for all members (duplicates)
    unique_titles           = []    #get all unique titles 
    grouped_members         = []    #group members by title (needs to nestled within title indent)
    inst_member_dic         = []    #list with double sublist where first item in first sublist is title and second item is a second list of all names with that title
    grouped_members_temp    = []
    
    
    #find all members
    
    
    for members in rok_position.objects.filter(institution=institution_detail):
        member_tag = members.person
        member_url = member_tag.get_absolute_url
        for e in rok_position.objects.filter(institution=institution_detail, person=member_tag):
            member_title = e.title 
            if member_title not in unique_titles:
                unique_titles.append(member_title)
    for title in unique_titles:
        grouped_members_temp = []
        for title_holder in rok_position.objects.filter(institution=institution_detail, title=title):
            title_holder = title_holder.person
            title_holder_name = title_holder.name
            title_holder_url = title_holder.get_absolute_url
            title_holder_photo = title_holder.full_resolution_photo
            grouped_members_temp.append([title_holder_name, title_holder_url, title_holder_photo])
        grouped_members = [title, grouped_members_temp]
        inst_member_dic.append(grouped_members)
    
    
    context = {
            
            'institution_name'      : institution_detail.name,
            'institution_korean'    : institution_detail.name_korean,
            'institution_function'  : institution_detail.function,
            'institution_add'       : institution_detail.additional_information,
            'inst_member_dic'       : inst_member_dic,
            'style_sheet'             : link_text,
            }
    
    
    return render(request, 'institution_page.html', context)



def article_list(request):

    article_list = []
    for e in article.objects.all():
        article_list.append(e)

    context = {

        'article_list'              : article_list, 
        'style_sheet'             : link_text,
                }
    
    return render(request, 'article_list.html', context)

def individual_list(request):
    individual_list = []
    for e in individual.objects.order_by('-update_date'):
        individual_list.append(e)

    context = {

        'individual_list'       : individual_list, 
        'style_sheet'           : link_text,
    }
    
    return render(request, 'individual_list.html', context)

def institution_list (request):
    institution_list = []
    for e in institution.objects.all():
        institution_list.append(e)
    context = {

        'institution_list '       : institution_list , 
        'style_sheet'             : link_text,

    }
    
    return render(request, 'institution_list.html', context)



