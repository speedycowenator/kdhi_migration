from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from trackers.models import overseas_tracker, inter_korean_tracker, overseas_topic, country_list
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



def heatmap_static(request):
    context = {
            'style_sheet'           : link_text,
            }
    return render(request, 'heatmap_static.html', context)

    

def overseas_tracker_detail(request, pk):
    tracker_item = overseas_tracker.objects.get(pk=pk)
    participant_list = []
    for participant in tracker_item.participant_DPRK.all():
        participant_name    = participant.name
        participant_link    = participant.get_absolute_url
        participant_photo   = participant.full_resolution_photo
        participant_list_temp = [participant_name, participant_link, participant_photo]
        participant_list.append(participant_list_temp)

    
    context = {
        
            'tracker_item' : tracker_item,
            'participant_list' : participant_list,
            'style_sheet' : link_text
            }
    return render(request, 'overseas_detail.html', context)

def inter_korean_tracker_detail(request, pk):
    tracker_item = inter_korean_tracker.objects.get(pk=pk)
    participant_list_dprk = []
    participant_list_rok = []

    for participant in tracker_item.participant_DPRK.all():
        participant_name    = participant.name
        participant_link    = participant.get_absolute_url
        participant_photo   = participant.icon
        participant_list_temp = [participant_name, participant_link, participant_photo]
        participant_list_dprk.append(participant_list_temp)
    for participant in tracker_item.participant_ROK.all():
        participant_name    = participant.name
        participant_link    = participant.get_absolute_url
        participant_photo   = participant.icon
        participant_list_temp = [participant_name, participant_link, participant_photo]
        participant_list_rok.append(participant_list_temp)
   
    event_DPRK_head = tracker_item.DPRK_head
    event_ROK_head  = tracker_item.ROK_head
    
    context = {
        
            'tracker_item'          : tracker_item,
            'participant_list_dprk' : participant_list_dprk,
            'participant_list_rok'  : participant_list_rok,
            'style_sheet'           : link_text,
            'event_DPRK_head'       : event_DPRK_head,
            'event_ROK_head'        : event_ROK_head,

            
            }
    return render(request, 'inter_korean_detail.html', context)

def inter_korean_tracker_list(request):
    recent_event    = inter_korean_tracker.objects.latest('update_date')
    events_list     = []
    for e in inter_korean_tracker.objects.order_by('update_date'):
        e_title                 = e.event_title
        e_date                  = e.event_date
        e_content               = e.MOU_description
        e_url                   = e.get_absolute_url
        e_rok_delegate_list     = []
        e_dprk_delegate_list    = []
        e_DPRK_head             = e.DPRK_head


        try: 
            for ee in e.participant_DPRK:
                e_dprk_delegate         = ee.participant_DPRK
                e_dprk_delegate_name    = e_dprk_delegate.name
                e_dprk_delegate_url     = e_dprk_delegate.get_absolute_url
                e_dprk_delegate_icon    = e_dprk_delegate.icon
                e_dprk_delegate         = [e_dprk_delegate_name, e_dprk_delegate_url, e_dprk_delegate_icon]
                e_dprk_delegate_list.append(e_dprk_delegate)
        except:
            pass

        e_ROK_head             = e.ROK_head

        
        try: 
            for ee in e.participant_DPRK:
                e_rok_delegate          = e.participant_ROK
                e_rok_delegate_name     = e_rok_delegate.name
                e_rok_delegate_url      = e_rok_delegate.get_absolute_url
                e_rok_delegate_icon     = e_rok_delegate.icon
                e_rok_delegate          = [e_rok_delegate_name, e_rok_delegate_url, e_rok_delegate_icon]
                e_rok_delegate_list.append(e_dprk_delegate)
        except:
            pass
        event_item = [e_title, e_date, e_content, e_url, e_ROK_head, e_DPRK_head]

        events_list.append(event_item)
    context = {
        'recent_event'  :   recent_event,
        'style_sheet'   :   link_text,
        'events_list'   :   events_list, 

    }
    return render(request, 'inter_korean.html', context)

def overseas_tracker_list(request):
    recent_event    = overseas_tracker.objects.latest('update_date')
    events_list     = []
    for e in overseas_tracker.objects.order_by('update_date'):
        events_list.append(e)
    context = {
        'recent_event'  :   recent_event,
        'style_sheet'   :   link_text,
        'events_list'   :   events_list, 

    }
    return render(request, 'overseas.html', context)

