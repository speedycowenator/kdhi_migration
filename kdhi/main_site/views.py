
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from main_site.models import dprk_institution_tag, glossary_item, individual, glossary_item, institution, position, rok_individual, rok_institution, rok_individual, rok_position, article
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
from django.core.paginator import Paginator

import bs4
import urllib.request

url = 'https://kdhi.webflow.io/'
#url = 'https://kdhi-archive-code-builder.webflow.io/'

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


def inter_korean_spending_2018(request):
    context = {
        'java_location'     : java_location,
        'style_sheet'       : link_text,
        'webflow_page_data' : webflow_page_data,
        'page_title'        : 'Inter-Korean Spending: 2018',


    }
    return render(request, 'static_pages/inter-korean-spending-2018.html', context)

def research_page(request):
    research_cards = []
    for e in article.objects.all():
        research_cards.append(e)
    featured_research_card =article.objects.latest('create_date')
    webflow_page_data = "5eb9f7c0c3ca3d253f5b738c"
    context = {
        'webflow_page_data'         : webflow_page_data,
        'base_site'                 : url,
        'java_location'             : java_location,
        'style_sheet'               : link_text,
        'research_cards'            : research_cards,
        'featured_research_card'    : featured_research_card,
        'page_title'                : 'Research',

    }
    return render(request, 'research.html', context)


def about_page(request):
    context = {
        'webflow_page_data' : webflow_page_data,
        'java_location'     : java_location,
        'style_sheet'       : link_text,
        'page_title'        : 'About',

    }
    return render(request, 'static_pages/about.html', context)


def glossary_detail(request, slug):
    glossary = glossary_item.objects.get(slug=slug)

    context = {
        'glossary_item'     : glossary,
        'java_location'     : java_location,
        'style_sheet'       : link_text,
        'webflow_page_data' : webflow_page_data,

    }
    return render(request, 'glossary_detail.html', context)


def article_detail(request, slug):
    article_ref = article.objects.get(slug=slug)



    context = {
        'style_sheet'           : link_text,
        'article'   : article_ref,
        'webflow_page_data' : webflow_page_data,
        }
        
    return render(request, 'article_detail.html', context)

def glossary_list(request):
    glossary = glossary_item.objects.all()

    context = {
        'glossary_list'     : glossary,
        'java_location'     : java_location,
        'style_sheet'       : link_text,
        'webflow_page_data' : webflow_page_data,

    }
    return render(request, 'glossary_list.html', context)


def homepage_view(request):

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
        'java_location'             : java_location,
        'latest_article'            : latest_article,
        'secondary_article_list'    : secondary_article_list,
        'glossary_list'             : glossary_list,
        'webflow_page_data' : webflow_page_data,

    }
    
    return render(request, 'static_pages/homepage.html', context)

def individual_detail(request, name):
    individual_detail = individual.objects.get(name__icontains=name)
    individual_positions = []
    s3_path_full    = "https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Leadership+Photos/Full+Resolution/"
    s3_path_icon    = "https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Leadership+Photos/1+x+1+Icons/"
    individual_name = individual_detail.name
    name_url_snip   = individual_name.replace(' ', '+')
    #name_url_snip   = name_url_snip.lower()
    img_full_res    = individual_detail.bs4_image_test
    img_icon        = s3_path_icon + name_url_snip + '.jpg'

    for individual_position in position.objects.filter(person=individual_detail):
        institution_tag = individual_position.institution
        inst_url = institution_tag.get_absolute_url
        individual_position_pair = [individual_position.institution, individual_position.title, inst_url, individual_position.position_status]
        individual_positions.append(individual_position_pair)
    page_title = individual_detail.name


 #need to add 'toggle' as a 'hide' class #}
    try: 
        if len(individual_detail.bio) > 0:
            bio_toggle = ''
        else: 
            bio_toggle = 'toggle'
    except: 
        bio_toggle = 'toggle'

    try: 
        if len(individual_detail.sources) > 0:
            source_toggle = ''
        else: 
            source_toggle = 'toggle'
    except: 
        source_toggle = 'toggle'
    context = {
            'individual_detail'     : individual_detail,
            'individual_name'       : individual_detail.name,
            'individual_photo'      : img_full_res,
            'individual_birthday'   : individual_detail.birthday,
            'individual_education'  : individual_detail.education,
            'individual_biography'  : individual_detail.bio,
            'individual_sources'    : individual_detail.sources,
            'individual_hometown'   : individual_detail.hometown,
            'individual_positions'  : individual_positions,
            'java_location'     : java_location,
            'java_location'     : java_location,
            'style_sheet'       : link_text,
            'page_title'            : page_title,
            'bio_toggle'            : bio_toggle,
            'source_toggle'         : source_toggle,
            'webflow_page_data' : webflow_page_data,
            
            }
    return render(request, 'biographic_page.html', context)


def institution_detail(request, name):
    institution_detail  = institution.objects.get(name__icontains=name)
      
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
        for title_holder in position.objects.filter(institution=institution_detail, title=title, position_status="Active") | position.objects.filter(institution=institution_detail, title=title, position_status="Likely"):
            title_holder = title_holder.person
            title_holder_name = title_holder.name
            title_holder_url = title_holder.get_absolute_url
            s3_path_full    = "https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Leadership+Photos/Full+Resolution/"
            name_url_snip   = title_holder_name.replace(' ', '+')
            img_icon        = title_holder.get_image_icon
            grouped_members_temp.append([title_holder_name, title_holder_url, img_icon])
        grouped_members = [title, grouped_members_temp]
        inst_member_dic.append(grouped_members)

    try: 
        if len(institution_detail.additional_figures) > 0:
            add_fig_toggle = ''
        else: 
            add_fig_toggle = 'toggle'
    except: 
        add_fig_toggle = 'toggle'

    try: 
        if len(institution_detail.organization_structure) > 0:
            org_toggle = ''
        else: 
            org_toggle = 'toggle'
    except: 
        org_toggle = 'toggle'

    try: 
        if len(institution_detail.additional_information) > 0:
            add_in_toggle = ''
        else: 
            add_in_toggle = 'toggle'
    except: 
        add_in_toggle = 'toggle'

    try: 
        if len(institution_detail.sources_add) > 0:
            source_toggle = ''
        else: 
            source_toggle = 'toggle'
    except: 
        source_toggle = 'toggle'

    page_title = institution_detail.name
    ministry_institution_list = []
    for inst in institution.objects.filter(Q(name__icontains="Ministry") | Q(name__icontains="Committee") | Q(name__icontains="Central")).all(): 
        ministry_institution_list.append(inst)
    context = {
            
            'ministry_institution_list' : ministry_institution_list,
            'institution_name'      : institution_detail.name,
            'institution_figs'      : institution_detail.additional_figures,
            'institution_src'       : institution_detail.sources_add,
            'institution_org'       : institution_detail.organization_structure,
            'institution_korean'    : institution_detail.name_korean,
            'institution_function'  : institution_detail.function,
            'institution_add'       : institution_detail.additional_information,
            'inst_member_dic'       : inst_member_dic,
            'java_location'     : java_location,
            'style_sheet'       : link_text,
            'page_title'            : page_title,
            'source_toggle'         : source_toggle,
            'add_in_toggle'         : add_in_toggle,
            'org_toggle'            : org_toggle, 
            'add_fig_toggle'        : add_fig_toggle,
            'webflow_page_data' : webflow_page_data,

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
    if len(individual_detail.awards_items) > 10:
        toggle_awards = ''
    else:
        toggle_awards = '-off'
    if len(individual_detail.education_items) > 10:
        toggle_education = ''
    else:
        toggle_education = '-off'
    if len(individual_detail.career_items) > 10:
        toggle_career = ''
    else:
        toggle_career = '-off'


    toggle_career
    context = {
            'individual_name'       : individual_detail.name,
            'individual_photo'      : individual_detail.get_image_icon,
            'individual_positions'  : individual_positions,
            'individual_detail'     : individual_detail,
            'java_location'     : java_location,
            'style_sheet'       : link_text,
            'toggle_education'      : toggle_education,
            'toggle_awards'         : toggle_awards, 
            'toggle_career'         : toggle_career,  
            'webflow_page_data' : webflow_page_data,
            }
    return render(request, 'rok_biographic_page.html', context)

 
def rok_institution_detail(request, slug):
    institution_detail      = rok_institution.objects.get(slug=slug)
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
            'inst_member_dic'       : inst_member_dic,
            'institution_history'   : institution_detail.history,
            'institution_url'       : institution_detail.official_webpage,
            'institution_src'       : institution_detail.sources_add,
            'java_location'     : java_location,
            'style_sheet'       : link_text,
            'webflow_page_data' : webflow_page_data,
            }
    
    
    return render(request, 'rok_institution_page.html', context)



def article_list(request):

    article_list = []
    for e in article.objects.all():
        article_list.append(e)

    context = {

        'article_list'      : article_list, 
        'java_location'     : java_location,
        'style_sheet'       : link_text,
        'webflow_page_data' : webflow_page_data,
                }
    
    return render(request, 'article_list.html', context)

def individual_list(request):
    individual_list = []

    individual_positions_one = []
    individual_positions_two = []
    individual_positions_three = []
    if request.method == 'GET':
        for individual_lookup in individual.objects.order_by('name'):
            individual_institution_list = []
            for individual_position in position.objects.filter(person=individual_lookup):
                individual_position_pair = [individual_position.institution, individual_position.title]
                individual_institution_list.append(individual_position_pair)
            individual_list.append([individual_lookup, individual_institution_list])
    if request.method == 'POST':
        search_text = request.POST.get("search_text")
        for individual_lookup in individual.objects.filter(name__icontains=search_text).order_by('name'):
            individual_institution_list = []
            for individual_position in position.objects.filter(person=individual_lookup):
                individual_position_pair = [individual_position.institution, individual_position.title]
                individual_institution_list.append(individual_position_pair)
            individual_list.append([individual_lookup, individual_institution_list])   
    featured_one    = individual.objects.get(name="Choe Ryong Hae")
    for individual_position in position.objects.filter(person=featured_one):
        institution_tag = individual_position.institution
        inst_url = institution_tag.get_absolute_url
        individual_position_pair = [individual_position.institution, individual_position.title, inst_url, individual_position.position_status]
        individual_positions_one.append(individual_position_pair)

    featured_two    = individual.objects.get(name="An Jong Su")
    for individual_position in position.objects.filter(person=featured_two):
        institution_tag = individual_position.institution
        inst_url = institution_tag.get_absolute_url
        individual_position_pair = [individual_position.institution, individual_position.title, inst_url, individual_position.position_status]
        individual_positions_two.append(individual_position_pair)

    featured_three  = individual.objects.get(name="Kim Yo Jong")
    for individual_position in position.objects.filter(person=featured_three):
        institution_tag = individual_position.institution
        inst_url = institution_tag.get_absolute_url
        individual_position_pair = [individual_position.institution, individual_position.title, inst_url, individual_position.position_status]
        individual_positions_three.append(individual_position_pair)
    
    featured_card_one   = [featured_one, individual_positions_one]
    featured_card_two   = [featured_two, individual_positions_two]
    featured_card_three = [featured_three, individual_positions_three]

    featured_cards = [featured_card_one, featured_card_two, featured_card_three] 


    paginator = Paginator(individual_list, 50) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    webflow_page_data = '5eb9f7c0c3ca3d06cb5b7499'
    context = {
        'featured_cards'        : featured_cards,
        'page_obj'              : page_obj,
        'individual_list'       : individual_list, 
        'java_location'     : java_location,
        'style_sheet'           : link_text,
        'webflow_page_data'     : webflow_page_data,
    }
    
    return render(request, 'individual_list.html', context)

def dprk_institution_landing(request):
    if request.method == 'GET':
        qs_complex_list = institution.objects.all()
        quicksearch_toggle = 'on'
        search_text = "e.g. 'Ministry of Foreign Affairs' or 'foreign'"
    elif request.method == 'POST':
        search = request.POST.get("search")
        function_tag_refine = request.POST.get("function_tags")
        if search == '' and function_tag_refine == '':
            qs_complex_list = institution.objects.all()
            quicksearch_toggle = 'on'
            search_text = "e.g. 'Ministry of Foreign Affairs' or 'foreign'"
        else:
            if function_tag_refine == 'All':
                quicksearch_inst_list   = institution.objects.filter(name__icontains=search)
                qs_complex_list         = []

                if len(quicksearch_inst_list) == 0:
                    quicksearch_toggle = 'off'
                    search_text = "No results. Try another keyword or navigate for an institution in the section above."
                else:
                    quicksearch_toggle = 'on'
                    search_text = search
                    qs_complex_list = quicksearch_inst_list
            else:
                quicksearch_inst_list   = institution.objects.filter(name__icontains=search, function_tags__name=function_tag_refine)
                qs_complex_list         = []
                if len(quicksearch_inst_list) == 0:
                    quicksearch_toggle = 'off'
                    search_text = "No results. Try another keyword or navigate for an institution in the section above."
                else:
                    quicksearch_toggle = 'on'
                    search_text = search
                    qs_complex_list = quicksearch_inst_list
                #for quicksearch_inst in quicksearch_inst_list:
                    #chief_position      = position.objects.filter(institution=quicksearch_inst, position_rank=0).first()
                    #try: 
                    #    chief_official      = chief_position.person
                    #    qs_complex_list.append([quicksearch_inst,chief_official])
                    #except:
                    #    qs_complex_list.append([quicksearch_inst])      

    tag_options = dprk_institution_tag.objects.all()

    paginator = Paginator(qs_complex_list, 50) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ministry_institution_list = []
    for inst in institution.objects.filter(Q(name__icontains="Ministry") | Q(name__icontains="Central")): 
        try: 
            chief_position = position.objects.filter(institution=inst, position_rank=0).first()
            chief_official = chief_position.person
        except:
            chief_official = ''
        ministry_institution_list.append([inst, chief_official])


    webflow_page_data = '5eb9f7c0c3ca3d06cb5b7499'
    context = {
        'ministry_institution_list' : ministry_institution_list,
        'search_text'           : search_text,
        'tag_options'           : tag_options,
        'quicksearch_toggle'    : quicksearch_toggle,
        'java_location'     : java_location,
        'style_sheet'           : link_text,
        'page_obj'              : page_obj,
        'webflow_page_data'     : webflow_page_data,
    }
    
    return render(request, 'dprk_institution_landing.html', context)

def rok_institution_landing(request): 
    if request.method == 'GET':
            qs_complex_list = rok_institution.objects.all()
            quicksearch_toggle = 'on'
            search_text = "e.g. 'Ministry of Foreign Affairs' or 'foreign'"
    elif request.method == 'POST':
        search = request.POST.get("search")
        function_tag_refine = request.POST.get("function_tags")
        if search == '':
            qs_complex_list = rok_institution.objects.all()
            quicksearch_toggle = 'on'
            search_text = "e.g. 'Ministry of Foreign Affairs' or 'foreign'"
        else:
            if function_tag_refine == 'All':
                quicksearch_inst_list   = rok_institution.objects.filter(name__icontains=search)
                qs_complex_list         = []

                if len(quicksearch_inst_list) == 0:
                    quicksearch_toggle = 'off'
                    search_text = "No results. Try another keyword or navigate for an rok_institution in the section above."
                else:
                    quicksearch_toggle = 'on'
                    search_text = search
                    qs_complex_list = quicksearch_inst_list
            else:
                quicksearch_inst_list   = rok_institution.objects.filter(name__icontains=search)
                qs_complex_list         = []
                if len(quicksearch_inst_list) == 0:
                    quicksearch_toggle = 'off'
                    search_text = "No results. Try another keyword or navigate for an rok_institution in the section above."
                else:
                    quicksearch_toggle = 'on'
                    search_text = search
                    qs_complex_list = quicksearch_inst_list


    paginator = Paginator(qs_complex_list, 50) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    webflow_page_data = '5eb9f7c0c3ca3d06cb5b7499'
    context = {
        'search_text'           : search_text,
        'quicksearch_toggle'    : quicksearch_toggle,
        'java_location'         : java_location,
        'style_sheet'           : link_text,
        'page_obj'              : page_obj,
        'webflow_page_data'     : webflow_page_data,
    }
    
    return render(request, 'rok_institution_landing.html', context)


'''

        pass    
 
    elif request.method == 'POST':
        pass
'''

def rok_individual_list(request):
    rok_individual_list = []

    rok_individual_rok_positions_one = []
    rok_individual_rok_positions_two = []
    rok_individual_rok_positions_three = []
    if request.method == 'GET':
        for rok_individual_lookup in rok_individual.objects.order_by('name'):
            rok_individual_institution_list = []
            for rok_individual_rok_position in rok_position.objects.filter(person=rok_individual_lookup):
                rok_individual_rok_position_pair = [rok_individual_rok_position.institution, rok_individual_rok_position.title]
                rok_individual_institution_list.append(rok_individual_rok_position_pair)
            rok_individual_list.append([rok_individual_lookup, rok_individual_institution_list])
    if request.method == 'POST':
        search_text = request.POST.get("search_text")
        for rok_individual_lookup in rok_individual.objects.filter(name__icontains=search_text).order_by('name'):
            rok_individual_institution_list = []
            for rok_individual_rok_position in rok_position.objects.filter(person=rok_individual_lookup):
                rok_individual_rok_position_pair = [rok_individual_rok_position.institution, rok_individual_rok_position.title]
                rok_individual_institution_list.append(rok_individual_rok_position_pair)
            rok_individual_list.append([rok_individual_lookup, rok_individual_institution_list])   
   
    featured_one    = rok_individual.objects.get(name="Choo Mi-ae")
    for rok_individual_rok_position in rok_position.objects.filter(person=featured_one):
        institution_tag = rok_individual_rok_position.institution
        inst_url = institution_tag.get_absolute_url
        rok_individual_rok_position_pair = [rok_individual_rok_position.institution, rok_individual_rok_position.title]
        rok_individual_rok_positions_one.append(rok_individual_rok_position_pair)

    featured_two    = rok_individual.objects.get(name="Baek Seung-geun")
    for rok_individual_rok_position in rok_position.objects.filter(person=featured_two):
        institution_tag = rok_individual_rok_position.institution
        inst_url = institution_tag.get_absolute_url
        rok_individual_rok_position_pair = [rok_individual_rok_position.institution, rok_individual_rok_position.title]
        rok_individual_rok_positions_two.append(rok_individual_rok_position_pair)

    featured_three  = rok_individual.objects.get(name="Chin Yong")
    for rok_individual_rok_position in rok_position.objects.filter(person=featured_three):
        institution_tag = rok_individual_rok_position.institution
        inst_url = institution_tag.get_absolute_url
        rok_individual_rok_position_pair = [rok_individual_rok_position.institution, rok_individual_rok_position.title]
        rok_individual_rok_positions_three.append(rok_individual_rok_position_pair)
    
    featured_card_one   = [featured_one, rok_individual_rok_positions_one]
    featured_card_two   = [featured_two, rok_individual_rok_positions_two]
    featured_card_three = [featured_three, rok_individual_rok_positions_three]

    featured_cards = [featured_card_one, featured_card_two, featured_card_three] 


    paginator = Paginator(rok_individual_list, 50) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    webflow_page_data = '5eb9f7c0c3ca3de5d55b7494'
    context = {
        'featured_cards'        : featured_cards,
        'java_location'         : java_location,
        'page_obj'              : page_obj,
        'ndividual_list'        : rok_individual_list, 
        'style_sheet'           : link_text,
        'webflow_page_data'     : webflow_page_data,
    }
    
    return render(request, 'rok_individual_list.html', context)