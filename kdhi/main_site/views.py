
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
        'latest_article'            : latest_article,
        'secondary_article_list'    : secondary_article_list,
        'glossary_list'             : glossary_list,

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
            'style_sheet'           : link_text,
            'page_title'            : page_title,
            'bio_toggle'            : bio_toggle,
            'source_toggle'         : source_toggle,
            
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
        for title_holder in position.objects.filter(institution=institution_detail, title=title, position_status="Active"):
            title_holder = title_holder.person
            title_holder_name = title_holder.name
            title_holder_url = title_holder.get_absolute_url
            s3_path_full    = "https://kdhi-resources.s3.amazonaws.com/kdhi.org/Assets/Leadership+Photos/Full+Resolution/"
            name_url_snip   = title_holder_name.replace(' ', '+')
            img_icon        = title_holder.get_image_icon
            grouped_members_temp.append([title_holder_name, title_holder_url, img_icon])
        grouped_members = [title, grouped_members_temp]
        inst_member_dic.append(grouped_members)

    #----------------------- Related / Tag selection
    tripartite_tag_inst = institution_detail.tripartite_tag
    sphere_tag_inst     = institution_detail.sphere_tag
    sector_tag_insts    = [institution_detail.sector_tag_1, institution_detail.sector_tag_2]
    related_inst_list   = []
    related_party       = []
    related_state       = []
    related_military    = []

    for tag in sector_tag_insts:
        if len(tag) > 1:
            for i in institution.objects.filter(sector_tag_1=tag):
                if i != institution_detail:
                    related_inst_list.append(i)
            for i in institution.objects.filter(sector_tag_2=tag):
                if i != institution_detail:
                    related_inst_list.append(i)
    for inst in related_inst_list:
        if inst.tripartite_tag == 'State':
            related_state.append(inst)
        if inst.tripartite_tag == "Party":
            related_party.append(inst)
        if inst.tripartite_tag == "Military":
            related_military.append(inst)

    if len(related_party) == 0:
        related_party       = "No related institutions"
    if len(related_state) == 0:
        related_state       = "No related institutions"
    if len(related_military) == 0:
        related_military       = "No related institutions"

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
    context = {
            
            'institution_name'      : institution_detail.name,
            'institution_figs'      : institution_detail.additional_figures,
            'institution_src'       : institution_detail.sources_add,
            'institution_org'       : institution_detail.organization_structure,
            'institution_korean'    : institution_detail.name_korean,
            'institution_function'  : institution_detail.function,
            'institution_add'       : institution_detail.additional_information,
            'inst_member_dic'       : inst_member_dic,
            'style_sheet'           : link_text,
            'tripartite_tag_inst'   : tripartite_tag_inst,
            'sphere_tag_inst'       : sphere_tag_inst,
            'sector_tag_insts'      : sector_tag_insts,
            'related_inst'          : related_inst_list,
            'related_party'         : related_party,
            'related_state'         : related_state,
            'related_military'      : related_military,
            'page_title'            : page_title,
            'source_toggle'         : source_toggle,
            'add_in_toggle'         : add_in_toggle,
            'org_toggle'            : org_toggle, 
            'add_fig_toggle'        : add_fig_toggle,

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
            'style_sheet'           : link_text,
            'toggle_education'      : toggle_education,
            'toggle_awards'         : toggle_awards, 
            'toggle_career'         : toggle_career  
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
            'style_sheet'           : link_text,
            }
    
    
    return render(request, 'rok_institution_page.html', context)



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
        search_text = "e.g. 'Ministry of Foreign Affairs' or 'foreign'"
    elif request.method == 'POST':
        search = request.POST.get("search")
        if search == '':
            qs_complex_list = []
            quicksearch_toggle = 'off'
            search_text = "No results. Try another keyword or navigate for an institution in the section above."
        else:
            quicksearch_inst_list   = institution.objects.filter(name__icontains=search)
            qs_complex_list         = []
            if len(quicksearch_inst_list) == 0:
                quicksearch_toggle = 'off'
                search_text = "No results. Try another keyword or navigate for an institution in the section above."

                pass
            else:
                quicksearch_toggle = 'on'
                search_text = search
                for quicksearch_inst in quicksearch_inst_list:
                    chief_position      = position.objects.filter(institution=quicksearch_inst, position_rank=0).first()
                    try: 
                        chief_official      = chief_position.person
                        qs_complex_list.append([quicksearch_inst,chief_official])
                    except:
                        qs_complex_list.append([quicksearch_inst])      


    context = {
        'search_text'           : search_text,
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

def rok_individual_list(request):
    individual_list = []
    for e in rok_individual.objects.order_by('name'):
        individual_list.append(e)

    context = {

        'individual_list'       : individual_list, 
        'style_sheet'           : link_text,
    }

    return render(request, 'individual_list.html', context)