
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from main_site.models import individual, institution, position
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
            'inst_member_dic'   : inst_member_dic,

            }
    
    
    return render(request, 'institution_page.html', context)



