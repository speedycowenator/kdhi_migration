from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from trackers.models import overseas_tracker
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


def tracker_detail(request, pk):
    tracker_item = overseas_tracker.objects.get(pk=pk)
    
    
    context = {
        
            'tracker_item' : tracker_item,
            
            
            }
    return render(request, 'tracker_detail.html', context)


