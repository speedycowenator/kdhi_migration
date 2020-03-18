from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from trackers.models import overseas_tracker, inter_korean_tracker
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



def tracker_detail(request, pk):
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
        participant_photo   = participant.full_resolution_photo
        participant_list_temp = [participant_name, participant_link, participant_photo]
        participant_list_dprk.append(participant_list_temp)
    for participant in tracker_item.participant_ROK.all():
        participant_name    = participant.name
        participant_link    = participant.get_absolute_url
        participant_photo   = participant.full_resolution_photo
        participant_list_temp = [participant_name, participant_link, participant_photo]
        participant_list_rok.append(participant_list_temp)
    
    context = {
        
            'tracker_item' : tracker_item,
            'participant_list_dprk' :  participant_list_dprk,
            'participant_list_rok' :  participant_list_rok,
            'style_sheet' : link_text

            
            }
    return render(request, 'inter_korean_detail.html', context)



