# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('db/',views.database,name='database'),
    path('edit/<int:r_id>/',views.edit_form,name='edit_form'),
    path('delete/<int:r_id>/',views.delete_rec,name='delete_rec'),
    path('view_charts/',views.view_charts,name='view_charts'),
    path('ajax_charts/',views.ajax_charts,name='ajax_charts')

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
