# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:45:35 2020

@author: Sam
"""

# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from news_archive.models import article_model, profile, nonuser_email_subscriptions
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

from django.conf.urls.static import static

def search_redirect(request):
    return HttpResponseRedirect("/state-media-archive/search-results")

def no_account_subscribe(request):
    return_variable_check = False
    if request.method == 'POST':
        subscription_email = request.POST.get('sub_email')
        try:
            nonuser_email_subscriptions.objects.filter(email=subscription_email)
            return_variable = 'Already registered'      
            return_variable_check = True

        except:
            b = nonuser_email_subscriptions(email=subscription_email)
            b.save()
            return_variable = 'Registered!'
            return_variable_check = True
    else:
        return_variable_check = True
        return_variable = "Oops! An error occured. Refresh page and try again."
    model = article_model
    publication_dictionary = {
        'kcna'  : 'KCNA',
        'rs'    : 'Rodong Sinmun',
        'all'   : ''

    }

    template_name = 'index/search_results.html'
    checked_one_week        = ''
    checked_one_month       = ''
    checked_six_months      = ''
    checked_one_year        = ''
    checked_five_years      = ''
    checked_all             = ''
    checked_kcna            = ''
    checked_rs              = ''
    checked_all_publication = ''
    checked_sort_asc        = ''
    checked_sort_dsc        = ''
    checked_sort_author     = ''
    checked_sort_date       = ''
    checked_sort_title      = ''
    text_search_1           = ''
    title_search_1          = ''
    date_select             = '1997-01-01'
    publication             = ''


    text_search_1 = request.GET.get('text_search_1')
    title_search_1    = request.GET.get('title_search_1')
    if text_search_1 == None:
        text_search_1 = ' '
    author = request.GET.get('author')
    if author == None:
        author = ''

    #--------- timestamp filter -------------
    if request.GET.get('date_select') != None:
        date_select = request.GET.get('date_select')
        time_period_selections = {
            'one_week'      : now - timedelta(days=7),
            'one_month'     : now - timedelta(weeks=4),
            'six_months'    : now - timedelta(weeks=24),
            'one_year'      : now - timedelta(weeks=52),
            'five_years'    : now - timedelta(weeks=260),
            'all'           : '1997-01-01',
        }
        filter_date = time_period_selections[date_select]
        if date_select == 'one_week':
            checked_one_week = 'checked="checked"'
        elif date_select == 'one_month':
            checked_one_month = 'checked="checked"'
        elif date_select == 'six_months':
            checked_six_months = 'checked="checked"'
        elif date_select == 'one_year':
            checked_one_year = 'checked="checked"'
        elif date_select == 'five_years':
            checked_five_years = 'checked="checked"'
        elif date_select == 'all':
            checked_all = 'checked="checked"'

    #---------- publication filter -----------
    publication = request.GET.get('publication')
    if request.GET.get('publication') != None:
        publication = request.GET.get('publication')
        if publication == 'kcna':
            checked_kcna = 'checked="checked"'

        elif publication == 'rs':
            checked_rs = 'checked="checked"'

        elif publication == 'all':
            checked_all_publication = 'checked="checked"'

    filter_order        = request.GET.get('sort_order')
    if filter_order == '-':
        checked_sort_dsc        = 'selected="selected"'
    else:
        checked_sort_asc       = 'selected="selected"'

    filter_mechanism    = request.GET.get('sort_object')
    if filter_mechanism == 'author':
        checked_sort_author      = 'selected="selected"'
    elif filter_mechanism == 'date_publication':
        checked_sort_date       = 'selected="selected"'
    elif filter_mechanism == 'title':
        checked_sort_title      = 'selected="selected"'


    if request.GET.get('date_select') == None:
        filter_date = '1997-01-01'
        checked_all = 'checked="checked"'
    if publication == None:
        publication = 'all'
        checked_all_publication = 'checked="checked"'

    if filter_order == None:
        filter_order = '-'
        checked_sort_dsc       = 'selected="selected"'

    if filter_mechanism == None:
        filter_mechanism = 'date_publication'
        checked_sort_date       = 'selected="selected"'

    filter_function     = filter_order + filter_mechanism
    publication_true = publication_dictionary[publication]

    try:
        article_list = article_model.objects.order_by(filter_function).filter(Q(summary__icontains=text_search_1)).filter(Q(title__icontains=title_search_1)).filter(Q(date_publication__gte=filter_date)).filter(Q(author__icontains=publication_true))
    except:
        article_list = ''
        title_search_1 = ''
        text_search_1 = ''
    context = {
        'checked_one_week'      :   checked_one_week,
        'checked_one_month'     :   checked_one_month,
        'checked_six_months'    :   checked_six_months,
        'checked_one_year'      :   checked_one_year,
        'checked_five_years'    :   checked_five_years,
        'checked_all'           :   checked_all,
        'checked_kcna'            : checked_kcna,
        'checked_rs'              : checked_rs,
        'checked_all_publication' : checked_all_publication,
        'checked_sort_asc'        : checked_sort_asc,
        'checked_sort_dsc'        : checked_sort_dsc,
        'checked_sort_author'     : checked_sort_author,
        'checked_sort_date'       : checked_sort_date,
        'checked_sort_title'      : checked_sort_title,
        'author' : author,
        'title_search_1' : title_search_1,
        'article_list' : article_list,
        'text_search_1' : text_search_1,
        'publication': publication_true,
        'filter_date' : filter_date,
        'return_variable' : return_variable,
        'return_variable_check' : return_variable_check,
    }

    return render(request, 'index/search_results.html', context)

def search_results(request):
    return_variable_check = False
    return_variable = None
    if request.method == 'POST':
        subscription_email = request.POST.get('sub_email')
        try:
            account =  nonuser_email_subscriptions.objects.get(email=subscription_email)
            return_variable = 'That email is already registered. Try checking your email account spam filter!'
            return_variable_check = True

        except:
            b = nonuser_email_subscriptions(email=subscription_email)
            b.save()
            return_variable = 'Registered!'
            return_variable_check = True

    model = article_model
    publication_dictionary = {
        'kcna'  : 'KCNA',
        'rs'    : 'Rodong Sinmun',
        'all'   : ''

    }

    template_name = 'index/search_results.html'
    checked_one_week        = ''
    checked_one_month       = ''
    checked_six_months      = ''
    checked_one_year        = ''
    checked_five_years      = ''
    checked_all             = ''
    checked_kcna            = ''
    checked_rs              = ''
    checked_all_publication = ''
    checked_sort_asc        = ''
    checked_sort_dsc        = ''
    checked_sort_author     = ''
    checked_sort_date       = ''
    checked_sort_title      = ''

    text_search_1           = ''
    title_search_1          = ''
    date_select             = '1997-01-01'
    publication             = ''


    text_search_1 = request.GET.get('text_search_1')
    title_search_1    = request.GET.get('title_search_1')

    #--------- timestamp filter -------------
    if request.GET.get('date_select') != None:
        date_select = request.GET.get('date_select')
        time_period_selections = {
            'one_week'      : now - timedelta(days=7),
            'one_month'     : now - timedelta(weeks=4),
            'six_months'    : now - timedelta(weeks=24),
            'one_year'      : now - timedelta(weeks=52),
            'five_years'    : now - timedelta(weeks=260),
            'all'           : '1997-01-01',
        }
        filter_date = time_period_selections[date_select]
        if date_select == 'one_week':
            checked_one_week = 'checked="checked"'
        elif date_select == 'one_month':
            checked_one_month = 'checked="checked"'
        elif date_select == 'six_months':
            checked_six_months = 'checked="checked"'
        elif date_select == 'one_year':
            checked_one_year = 'checked="checked"'
        elif date_select == 'five_years':
            checked_five_years = 'checked="checked"'
        elif date_select == 'all':
            checked_all = 'checked="checked"'

    #---------- publication filter -----------
    publication = request.GET.get('publication')
    if request.GET.get('publication') != None:
        publication = request.GET.get('publication')
        if publication == 'kcna':
            checked_kcna = 'checked="checked"'

        elif publication == 'rs':
            checked_rs = 'checked="checked"'

        elif publication == 'all':
            checked_all_publication = 'checked="checked"'

    if request.GET.get('date_select') == None:
        filter_date = '1997-01-01'
        checked_all = 'checked="checked"'
    if publication == None:
        publication = 'all'
        checked_all_publication = 'checked="checked"'
    filter_order        = request.GET.get('sort_order')
    if filter_order == '-':
        checked_sort_dsc        = 'selected="selected"'
    else:
        checked_sort_asc       = 'selected="selected"'

    filter_mechanism    = request.GET.get('sort_object')
    if filter_mechanism == 'author':
        checked_sort_author      = 'selected="selected"'
    elif filter_mechanism == 'date_publication':
        checked_sort_date       = 'selected="selected"'
    elif filter_mechanism == 'title':
        checked_sort_title      = 'selected="selected"'



    if filter_order == None:
        filter_order = '-'
        checked_sort_dsc       = 'selected="selected"'

    if filter_mechanism == None:
        filter_mechanism = 'date_publication'
        checked_sort_date       = 'selected="selected"'

    filter_function     = filter_order + filter_mechanism
    publication_true = publication_dictionary[publication]
    
#    try:
    search_article_list_mutable = []
    if title_search_1 != None or text_search_1 != None:
        blank_search = False
        if text_search_1 == None:
            text_search_1 = ' '
        author = request.GET.get('author')
        if author == None:
            author = ''
        
        if title_search_1 == None:
            title_search_1 = ' '
        for article in article_model.objects.order_by(filter_function).filter(Q(summary__icontains=text_search_1)).filter(Q(title__icontains=title_search_1)).filter(Q(date_publication__gte=filter_date)).filter(Q(author__icontains=publication_true)):
            search_pk       = article.pk
            search_link     = article.get_absolute_url 
            search_date     = article.date_publication
            search_author   = article.author
            search_text     = article.summary           
            search_title    = article.title
            search_count = 0
            search_text_truncated = ''
          
            #search_highlighter section
            search_term = text_search_1
    
            html_tag_front = "<strong>"
            html_tag_back = "</strong>"
            
            full_text_sentences = search_text.split('. ')
            marked_search_text = '... '
            marked_search_text_truncated = ''
            line_count = 0
            for line in full_text_sentences:
                match = re.search(search_term, line)
                line_count += 1
                if match:
                    if line_count == 1:
                        marked_search_text = ''
                    line_highlights = line
                    highlighted_search_term = html_tag_front + search_term + html_tag_back
                    line_highlights = re.sub(search_term, highlighted_search_term, line_highlights)
                    marked_search_text += line_highlights + ' ... '
            for char in marked_search_text:
                if search_count <= 499:
                    marked_search_text_truncated += char
                    search_count +=1
                if search_count == 499: 
                    marked_search_text_truncated += '--'
                    search_count +=1
                else:
                    pass

    
            search_article_object = [search_pk, search_link, search_title, search_date, search_author, marked_search_text_truncated]
            search_article_list_mutable.append(search_article_object)
    else:
        blank_search = True
        if text_search_1 == None:
            text_search_1 = ' '
        author = request.GET.get('author')
        if author == None:
            author = ''
        
        if title_search_1 == None:
            title_search_1 = ' '

        
         
        
    context = {
        'checked_one_week'      :   checked_one_week,
        'checked_one_month'     :   checked_one_month,
        'checked_six_months'    :   checked_six_months,
        'checked_one_year'      :   checked_one_year,
        'checked_five_years'    :   checked_five_years,
        'checked_all'           :   checked_all,
        'checked_kcna'            : checked_kcna,
        'checked_rs'              : checked_rs,
        'checked_all_publication' : checked_all_publication,
        'checked_sort_asc'        : checked_sort_asc,
        'checked_sort_dsc'        : checked_sort_dsc,
        'checked_sort_author'     : checked_sort_author,
        'checked_sort_date'       : checked_sort_date,
        'checked_sort_title'      : checked_sort_title,
        'author' : author,
        'title_search_1' : title_search_1,
        'article_list' : search_article_list_mutable,
        'text_search_1' : text_search_1,
        'publication': publication_true,
        'filter_date' : filter_date,
        'return_variable' : return_variable,
        'return_variable_check' : return_variable_check,
        'blank_search'  : blank_search,
    }


    return render(request, 'index/search_results.html', context)



def ArticleDetailView(request, pk):
    model = article_model
    template_name = 'index/article_detail.html'     
    favorite_article_list = []
    try:
        favorite_command_test = request.GET.get('_')
        command_toggle = len(favorite_command_test) > 0
    except:
        command_toggle = False

    #is it a favorite? (carries variable article_favorited)
    article = article_model.objects.get(pk=pk)
    favorited_strings = []
    favorited_list_test = []
    article_favorited = False
    if command_toggle == False:
        try:
            favorite_string = request.user.profile.favorites
            favorite_string_list = favorite_string.split(',')
            favorite_article_list = article_model.objects.filter(pk__in=favorite_string_list)
            for oject in favorite_article_list:
                favorite_pk = oject.pk
                favorited_strings.append(favorite_pk)
                favorited_test = favorite_pk == pk
                favorited_list_test.append(favorited_test)
            if any(favorited_list_test) == True:
                article_favorited = True
        except:
            pass
    else:
        pass

    if command_toggle == True and favorite_command_test == '+': #favorite command sent
        show_button = 'unsubscribe'
        article_favorited = 'True'
        b3 = request.user.profile
        profile_favorites_update    = ''
        profile_favorites_string           = request.user.profile.favorites
        profile_favorites                  = profile_favorites_string.split(',')
        for favorites in profile_favorites:
            if favorites != str(article.pk):
                fav_different = True
            else:
                fav_different = False
        if fav_different == False:
            profile_favorites_update = profile_favorites_string
        else:
            for favorites in profile_favorites:
                if len(favorites) > 0:
                    profile_favorites_update += favorites + ','
            profile_favorites_update    += str(article.pk)
        b3.favorites = profile_favorites_update
        b3.save()

    elif command_toggle == True and favorite_command_test == '-': #unfavorite command sent
        show_button = 'subscribe'
        article_favorited = 'False'
        b3 = request.user.profile
        profile_favorites_string           = request.user.profile.favorites
        profile_favorites = profile_favorites_string.split(',')
        minus_removal_test_length   = len(profile_favorites)
        profile_favorites_update    = ''
        for favorites in profile_favorites:
            if favorites != str(article.pk) and len(favorites) > 0:
                profile_favorites_update += favorites + ','
        #if minus_removal_test_length > extra_minus_location and minus_removal_test_length % 2 != 0:
        #    profile_favorites_update = profile_favorites_update[0:extra_minus_location-1]
        b3.favorites = profile_favorites_update
        b3.save()
    elif command_toggle == False and article_favorited == True:
        show_button = 'unsubscribe'
    elif command_toggle == False and article_favorited == False:
        show_button = 'subscribe'
    else:
        show_button = 'None'


    context = {
    'article'           : article,
    'command_toggle'    : command_toggle,
    'favorite_status'   : article_favorited,
    'show_button'       : show_button
    }
    return render(request, 'index/article_detail.html', context)

def print_list(request):
    checked_sort_asc        = ''
    checked_sort_dsc        = ''
    checked_sort_author     = ''
    checked_sort_date       = ''
    checked_sort_title      = ''

    favorite_string = request.user.profile.favorites
    favorite_string_list_dirty = favorite_string.split(',')
    favorite_string_list = []
    for string in favorite_string_list_dirty:
        if len(string) >0:
            favorite_string_list.append(string)
        else:
            pass
    filter_function     = '-date_publication'
    favorite_article_list = article_model.objects.order_by(filter_function).filter(pk__in=favorite_string_list)
    context = {
        'article_list' : favorite_article_list,
        'checked_sort_asc'        : checked_sort_asc,
        'checked_sort_dsc'        : checked_sort_dsc,
        'checked_sort_author'     : checked_sort_author,
        'checked_sort_date'       : checked_sort_date,
        'checked_sort_title'      : checked_sort_title,

    }
    return render(request, "index/print_list.html", context)



def ProfileUpdate(request):
    model = profile
    profile_page = request.user.profile
    if request.method == 'POST':
        form  = ProfileUpdateForm(request.POST, instance=profile_page)
        if form.is_valid():
            profile_updates = form.save(commit=False) #not actually needed here, but leaving in so the code can accept changes to the request if needed
            profile_updates.save()
            return redirect('profile')

    else:
        form = ProfileUpdateForm(instance=profile_page)


    context = {
    'form' : form
    }
    return render(request, "accounts/ProfileUpdate.html", context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile_page(request):
    checked_sort_asc        = ''
    checked_sort_dsc        = ''
    checked_sort_author     = ''
    checked_sort_date       = ''
    checked_sort_title      = ''

    favorite_string = request.user.profile.favorites
    favorite_string_list_dirty = favorite_string.split(',')
    favorite_string_list = []
    for string in favorite_string_list_dirty:
        if len(string) >0:
            favorite_string_list.append(string)
        else:
            pass
    filter_order        = request.GET.get('sort_order')
    if filter_order == '-':
        checked_sort_dsc        = 'selected="selected"'
    else:
        checked_sort_asc       = 'selected="selected"'

    filter_mechanism    = request.GET.get('sort_object')
    if filter_mechanism == 'author':
        checked_sort_author      = 'selected="selected"'
    elif filter_mechanism == 'date_publication':
        checked_sort_date       = 'selected="selected"'
    elif filter_mechanism == 'title':
        checked_sort_title      = 'selected="selected"'



    if filter_order == None:
        filter_order = '-'
        checked_sort_dsc       = 'selected="selected"'

    if filter_mechanism == None:
        filter_mechanism = 'date_publication'
        checked_sort_date       = 'selected="selected"'

    filter_function     = filter_order + filter_mechanism
    favorite_article_list = article_model.objects.order_by(filter_function).filter(pk__in=favorite_string_list)
    context = {
        'article_list' : favorite_article_list,
        'checked_sort_asc'        : checked_sort_asc,
        'checked_sort_dsc'        : checked_sort_dsc,
        'checked_sort_author'     : checked_sort_author,
        'checked_sort_date'       : checked_sort_date,
        'checked_sort_title'      : checked_sort_title,

    }
    return render (request, 'accounts/profile_page.html', context=context)
