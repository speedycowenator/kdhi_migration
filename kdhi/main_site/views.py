
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from main_site.models import glossary_item, individual, glossary_item, institution, position, rok_individual, rok_institution, rok_individual, rok_position, article
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
from django.utils.html import strip_tags

import bs4
import urllib.request

url = 'https://kdhi-archive-code-builder.webflow.io/event'

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find('link')


link_text = (link.get('href'))

def inter_korean_spending_2018(request):
    context = {
        'style_sheet'       : link_text,

    }
    return render(request, 'static_pages/inter-korean-spending-2018.html', context)

def research_page(request):
    research_cards = []
    for e in article.objects.all():
        research_cards.append(e)

    context = {
        'style_sheet'       : link_text,
        'research_cards'    : research_cards,

    }
    return render(request, 'research.html', context)


def about_page(request):
    context = {
        'style_sheet'       : link_text,

    }
    return render(request, 'static_pages/about.html', context)


def glossary_detail(request, slug):
    glossary = glossary_item.objects.get(slug=slug)

    context = {
        'glossary_item'     : glossary,
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

    collection_feature      = document_collection.objects.get(name="The June Struggle")
    collection_feature_url  = collection_feature.get_absolute_url
    latest_article          = article.objects.latest('update_date')

    secondary_article_list_full  = []
    secondary_glossary_list_full = []
    counter                 = 0
    for article_temp in article.objects.all():
        secondary_article_list_full.append(article_temp)
    secondary_article_list = secondary_article_list_full[1:3]
    for glossary_temp in glossary_item.objects.all():
        secondary_glossary_list_full.append(glossary_temp)
    glossary_list = secondary_glossary_list_full[0:8]

    context = {
        'style_sheet'               : link_text,
        'collection_feature'        : collection_feature,
        'latest_article'            : latest_article,
        'secondary_article_list'    : secondary_article_list,
        'glossary_list'             : glossary_list,

    }
    
    return render(request, 'static_pages/homepage.html', context)

def individual_detail(request, name):
    individual_detail = individual.objects.get(name=name)
    individual_positions = []
    s3_path_full    = "https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Leadership+Photos/Full+Resolution/"
    s3_path_icon    = "https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Leadership+Photos/1+x+1+Icons/"
    individual_name = individual_detail.name
    name_url_snip   = individual_name.replace(' ', '+')
    #name_url_snip   = name_url_snip.lower()
    img_full_res    = s3_path_full + name_url_snip + '.jpg'
    img_icon        = s3_path_icon + name_url_snip + '.jpg'

    for individual_position in position.objects.filter(person=individual_detail):
        institution_tag = individual_position.institution
        inst_url = institution_tag.get_absolute_url
        individual_position_pair = [individual_position.institution, individual_position.title, inst_url]
        individual_positions.append(individual_position_pair)
    
    context = {
            'individual_name'       : individual_detail.name,
            'individual_photo'      : img_full_res,
            'individual_birthday'   : individual_detail.birthday,
            'individual_education'  : individual_detail.education,
            'individual_biography'  : individual_detail.bio,
            'individual_sources'    : individual_detail.sources,
            'individual_hometown'   : individual_detail.hometown,
            'individual_positions'  : individual_positions,
            'style_sheet'           : link_text,
            
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
            s3_path_full    = "https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Leadership+Photos/Full+Resolution/"
            name_url_snip   = title_holder_name.replace(' ', '+')
            img_icon        = s3_path_full + name_url_snip + '.jpg'
            grouped_members_temp.append([title_holder_name, title_holder_url, img_icon])
        grouped_members = [title, grouped_members_temp]
        inst_member_dic.append(grouped_members)

           
    
    context = {
            
            'institution_name'      : institution_detail.name,
            'institution_figs'      : institution_detail.additional_figures,
            'institution_src'       : institution_detail.sources_add,
            'institution_org'       : institution_detail.organization_structure,
            'institution_korean'    : institution_detail.name_korean,
            'institution_function'  : institution_detail.function,
            'institution_add'       : institution_detail.additional_information,
            'inst_member_dic'       : inst_member_dic,
            'style_sheet'             : link_text,
            }
    
    
    return render(request, 'institution_page.html', context)


def rok_individual_detail(request, name_slug):
    individual_detail = rok_individual.objects.get(name_slug=name_slug)
    individual_positions = []
    for individual_position in rok_position.objects.filter(person=individual_detail):
        institution_tag = individual_position.institution
        inst_url = institution_tag.get_absolute_url
        individual_position_pair = [individual_position.institution, individual_position.title, inst_url]
        individual_positions.append(individual_position_pair)
    
    context = {
            'individual_name'       : individual_detail.name,
            'individual_photo'      : individual_detail.get_image_icon,
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
            title_holder_photo = title_holder.get_image_icon
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
    for e in individual.objects.order_by('name'):
        individual_list.append(e)

    context = {

        'individual_list'       : individual_list, 
        'style_sheet'           : link_text,
    }
    
    return render(request, 'individual_list.html', context)

def dprk_institution_landing(request):
    if request.method == 'GET':
        qs_complex_list = []
        quicksearch_toggle = 'off'

    elif request.method == 'POST':
        search = request.POST.get("search")
        if search == '':
            qs_complex_list = []
            quicksearch_toggle = 'off'
        else:
            quicksearch_inst_list   = institution.objects.filter(name__icontains=search)
            qs_complex_list         = []
            if len(quicksearch_inst_list) == 0:
                quicksearch_toggle = 'off'
                pass
            else:
                quicksearch_toggle = 'on'
                for quicksearch_inst in quicksearch_inst_list:
                    chief_position      = position.objects.filter(institution=quicksearch_inst, position_rank=0).first()
                    try: 
                        chief_official      = chief_position.person
                        qs_complex_list.append([quicksearch_inst,chief_official])
                    except:
                        qs_complex_list.append([quicksearch_inst])      


    context = {
        'quicksearch_toggle'    : quicksearch_toggle,
        'style_sheet'           : link_text,
        'quicksearch_inst_list' : qs_complex_list,
    }
    
    return render(request, 'dprk_institution_landing.html', context)

def rok_institution_landing(request): 
    if request.method == 'GET':
        qs_complex_list = []
        quicksearch_toggle = 'off'

    elif request.method == 'POST':
        search = request.POST.get("search")
        if search == '':
            qs_complex_list = []
            quicksearch_toggle = 'off'
        else:
            quicksearch_inst_list   = rok_institution.objects.filter(name__icontains=search)
            qs_complex_list         = []
            if len(quicksearch_inst_list) == 0:
                quicksearch_toggle = 'off'
                pass
            else:
                quicksearch_toggle = 'on'
                for quicksearch_inst in quicksearch_inst_list:
                    chief_position      = rok_position.objects.get(institution=quicksearch_inst, position_rank=0)
                    try: 
                        chief_official      = chief_position.person
                        qs_complex_list.append([quicksearch_inst,chief_official])
                    except:
                        qs_complex_list.append([quicksearch_inst]) 

    context = {
        'quicksearch_toggle'    : quicksearch_toggle,
        'style_sheet'           : link_text,
        'quicksearch_inst_list' : qs_complex_list,
    }
    
    return render(request, 'rok_institution_landing.html', context)



'''

        pass    

    elif request.method == 'POST':
        pass
'''