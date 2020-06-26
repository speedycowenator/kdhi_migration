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
import time
from datetime import date, timedelta
now = date.today()
import re
import bs4
import urllib.request
from trackers.models import overseas_tracker, inter_korean_tracker, overseas_topic, country_list
from media_archive.models import state_media_article
from django.core.paginator import Paginator


url = 'https://kdhi.webflow.io/'
#url = 'https://kdhi-archive-code-builder.webflow.io/institution-page'
webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find('link')
link_text = (link.get('href'))
webflow_page_data = '5eb9f7c0c3ca3dae2a5b7301'

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find_all('script')
link_count = len(link)
java_loc = link_count - 2
java_location = link[java_loc]
java_location = java_location.get('src')







def heatmap_static(request):
    context = {
            'style_sheet'           : link_text,
            'java_location'     : java_location,
            }
    return render(request, 'heatmap_static.html', context)

    

def overseas_tracker_detail(request, slug):
    tracker_item = overseas_tracker.objects.get(slug=slug)
    participant_list = []
    for participant in tracker_item.participant_DPRK.all():
        participant_name    = participant.name
        participant_link    = participant.get_absolute_url
        participant_photo   = participant.get_image_full
        participant_list_temp = [participant_name, participant_link, participant_photo]
        participant_list.append(participant_list_temp)
    try:
        if len(tracker_item.event_document) != 0:
            document_test = ''
        else:
            document_test = ' blank'
    except:
        document_test = ' blank'
    participant_test = ' blank'
    if len(participant_list) != 0:
        participant_test = ''
    image_test = ' blank'
    
    if len(tracker_item.event_photo) != 0:
        image_test = ''

    archive_link = ''
    archive_toggle = ' checked'



    try: 
        archive_link_object = state_media_article.objects.get(name=tracker_item.name)
        archive_link        = archive_link_object.get_absolute_url()
        archive_toggle      = '' 
    except:
        archive_toggle      = ' checked' 

    webflow_page_data = '5eb9f7c0c3ca3d46c75b738a'
    context = {
            'webflow_page_data' : webflow_page_data,
            'tracker_item'      : tracker_item,
            'participant_list'  : participant_list,
            'style_sheet'       : link_text,
            'document_test'     : document_test,
            'participant_test'  : participant_test,
            'image_test'        : image_test,
            'archive_toggle'    : archive_toggle,
            'archive_link'      : archive_link,
            'java_location'     : java_location,
            }
    return render(request, 'overseas_detail.html', context)

def inter_korean_tracker_detail(request, slug, itteration):
    tracker_item = inter_korean_tracker.objects.get(slug=slug, event_itteration=itteration)
    participant_list_dprk = []
    participant_list_rok = []
    event_DPRK_head = tracker_item.DPRK_head
    event_ROK_head  = tracker_item.ROK_head

    for participant in tracker_item.participant_DPRK.all():
        if participant != event_DPRK_head:
            participant_name    = participant.name
            participant_link    = participant.get_absolute_url
            participant_photo   = participant.get_image_icon
            participant_list_temp = [participant_name, participant_link, participant_photo]
            participant_list_dprk.append(participant_list_temp)
    for participant in tracker_item.participant_ROK.all():
        if participant != event_ROK_head:
            participant_name    = participant.name
            participant_link    = participant.get_absolute_url
            participant_photo   = participant.get_image_icon
            participant_list_temp = [participant_name, participant_link, participant_photo]
            participant_list_rok.append(participant_list_temp)
       
    
    context = {
        
            'tracker_item'          : tracker_item,
            'participant_list_dprk' : participant_list_dprk,
            'participant_list_rok'  : participant_list_rok,
            'style_sheet'           : link_text,
            'event_DPRK_head'       : event_DPRK_head,
            'event_ROK_head'        : event_ROK_head,
            'java_location'     : java_location,

            
            }
    return render(request, 'inter_korean_detail.html', context)

def inter_korean_tracker_list(request):
    recent_event    = inter_korean_tracker.objects.latest('update_date')
    events_list     = []
    for e in inter_korean_tracker.objects.order_by('-event_date'):
        e_title                 = e.name
        e_date                  = e.event_date
        e_content               = e.MOU_description
        e_url                   = e.get_absolute_url
        e_tag                   = [e.event_category]
        for e_subtag in e.event_subcategory.all():
            if e_subtag.name != "None":
                e_tag.append(e_subtag)
        e_ROK_head              = e.ROK_head
        e_DPRK_head             = e.DPRK_head
        for ee in e.meeting_topics.all():
            e_tag.append(ee)

        event_item = [e_title, e_date, e_content, e_url, e_tag, e_ROK_head, e_DPRK_head]

        events_list.append(event_item)


    paginator = Paginator(events_list, 50) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'recent_event'      : recent_event,
        'style_sheet'       : link_text,
        'events_list'       : events_list, 
        'java_location'     : java_location,
        'page_obj'          : page_obj,
    }
    return render(request, 'inter_korean.html', context)

def overseas_tracker_list(request):
    recent_event    = overseas_tracker.objects.latest('event_date')
    events_list     = []
    for e in overseas_tracker.objects.order_by('-event_date'):
        event_item_tags       = []
        for choice in e.overseas_topics.all():
            if len(choice.topic) > 1:
                event_item_tags.append(choice.topic)
        for choice in e.country_choices.all():
            if len(choice.country) > 1:
                event_item_tags.append(choice.country)
        events_list.append([e, event_item_tags])
    context = {
        'recent_event'  :   recent_event,
        'style_sheet'   :   link_text,
        'events_list'   :   events_list, 
        'java_location'     : java_location,

    }
    return render(request, 'overseas.html', context)

