# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import RecordingDetailForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count, Case, When, CharField


@login_required(login_url="/login/")
def index(request):
    if request.method == 'POST':
        fm = RecordingDetailForm(request.POST)
        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.created_by = request.user
            obj.save()
            messages.success(request,'Form saved successfully!')
        else:
            for field,errors in fm.errors.items():
                for error in errors:
                    messages.error(request,f"{field}: {error}")

    fm = RecordingDetailForm()
    return render(request,'home/ReForm.html',{'form':fm})


import random
from django.utils import timezone
from datetime import datetime, timedelta
from .models import RecordingDetail
def get_random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randrange(delta.days)
    return start_date + timedelta(days=random_days)

def populate_database():
    for _ in range(5):
        RecordingDetail.objects.create(
            name=f"User{random.randint(1, 1000)}",
            ethnicity=random.choice(RecordingDetail.Ethnicity)[0],
            age=random.randint(18, 65),
            # gender=random.choice(RecordingDetail.Gender)[0],
            gender='M',
            date=get_random_date(datetime(2023, 8, 1), datetime(2023, 10, 31)),
            height=random.randint(150, 200),
            beard=random.choice(RecordingDetail.Beard)[0],
            hair=random.choice(RecordingDetail.Hair)[0],
            eyecolour=random.choice(RecordingDetail.EyeColour)[0],
            workpackage=random.choice(RecordingDetail.WPGs)[0],
            workpackagetype=random.choice(RecordingDetail.WPTs)[0],
            carnumber=f"Car{random.randint(1, 100)}",
            carstatus=random.choice(RecordingDetail.CarStatus)[0],
            action=f"Action{random.randint(1, 5)}",
            clothingaccessories=random.choice(RecordingDetail.ClothingAccessoires)[0],
            glasses=random.choice(RecordingDetail.Glasses)[0],
            makeup=random.choice(RecordingDetail.Makeup)[0],
            recordingstatus=random.choice(RecordingDetail.RecordingStatus)[0],
        )
    print("Database populated with 50 random entries.")

# Make sure to call populate_database() where appropriate, for example in a custom management command or manually after server start.
# populate_database()
# from .models import RecordingDetail
# for i in RecordingDetail.objects.all():
#     i.delete()


from .models import RecordingDetail
@login_required(login_url="/login/")
def database(request):
    if request.user.username == 'root':
       recording_list = RecordingDetail.objects.all().order_by('-date')
    else:
        recording_list =  RecordingDetail.objects.filter(created_by=request.user).order_by('-date')
    p = Paginator(recording_list,7)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request,'home/database.html',{'page_obj':page_obj})

@login_required(login_url="/login/")
def edit_form(request,r_id):
    rec = RecordingDetail.objects.get(id=r_id)
    if request.method == 'POST':
        fm = RecordingDetailForm(request.POST,instance=rec)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Form updated successfully!')
            return redirect('database')
        else:
            for field,errors in fm.errors.items():
                for error in errors:
                    messages.error(request,f"{field}: {error}")
    fm = RecordingDetailForm(instance=rec)
    return render(request,'home/ReForm.html',{'form':fm})

    # pass

@login_required(login_url="/login/")
def delete_rec(request,r_id):
    rec = RecordingDetail.objects.get(id=r_id)
    rec.delete()
    return redirect('database')

@login_required(login_url="/login/")
def view_charts(request):
   if request.user.username=='root':
    return render(request,'home/chart-apex.html')

@login_required(login_url="/login/")
def ajax_charts(request):
    # getting query params from request
    start_date_str = request.GET.get('startDate')
    end_date_str = request.GET.get('endDate')
    ratio = request.GET.get('ratio')
    
    #formatting string date to datetime object
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    #filtering databse within that date range
    data_in_range = RecordingDetail.objects.filter(date__range=[start_date, end_date])


    def ethnicity():
        data = data_in_range.values('ethnicity').annotate(
            count=Count('id')).order_by('ethnicity')
        options = {
			'series': [],
			'labels': [],
		}
        for i in data:
            options['series'].append(i['count'])
            options['labels'].append(i['ethnicity'])
        return options

    def ethnicity_wise_gender():
        data = data_in_range.values('ethnicity').annotate(
            male_count=Count(Case(When(gender='M', then=1))),
            female_count=Count(Case(When(gender='F', then=1)))
        ).order_by('ethnicity')
        options = {
			'series': [
                {'name': 'Male','data': []},
                {'name': 'Female','data': []}
            ],
			'xaxis': {
				'categories': [],
			}
		}
        for i in data:
            options['series'][0]['data'].append(i['male_count'])
            options['series'][1]['data'].append(i['female_count'])
            options['xaxis']['categories'].append(i['ethnicity'])
        return options

    def date_wise_progress():
        data = data_in_range.values('date').annotate(
            count=Count('id')).order_by('date')
        options = {
			'series': [{
				'name': "Recordings",
				'data': []
			}],
			'xaxis': {
				'categories': [],
			}
		}
        for i in data:
            options['series'][0]['data'].append(i['count'])
            options['xaxis']['categories'].append(i['date'])
        return options

    def wp_wise_gender():
        data = data_in_range.values('workpackage').annotate(
            male_count=Count(Case(When(gender='M', then=1))),
            female_count=Count(Case(When(gender='F', then=1)))
        ).order_by('workpackage')
        options = {
            'series': [
                {'data': [],'name':'Male'},
                {'data': [],'name':'Female'}
            ],
            'xaxis': {
                'categories': [],
            }
        }
        for i in data:
            options['series'][0]['data'].append(i['male_count'])
            options['series'][1]['data'].append(i['female_count'])
            options['xaxis']['categories'].append(i['workpackage'])
        return options

    def gender():
        data = data_in_range.values('gender').annotate(
            count=Count('id')
        ).order_by('gender')

        options = {
            'series': [],
            'labels': []
        }
        for i in data:
            options['series'].append(i['count'])
            options['labels'].append(i['gender']) 

        return options

    final_data = {
        'ethnicity':ethnicity(),
        'gender':gender(),
        'ethnicity_wise_gender':ethnicity_wise_gender(),
        'wp_wise_gender':wp_wise_gender(),
        'date_wise_progress':date_wise_progress(),
    }

    return JsonResponse(final_data)




