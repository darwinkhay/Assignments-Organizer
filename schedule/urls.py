from django.urls import path

from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings

from django.conf.urls import url
from django.urls import re_path

app_name = 'schedule'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('assignment/form/', views.assignment_form, name='assignment_form'),
    path('assignment/list/', views.AssignmentListView.as_view(), name='assignment_list'),
    path('assignment/create', views.create_assignment, name='create_assignment'),
    path('assignment/delete/<int:assignment_id>', views.delete_assignment, name='delete_assignment'),
    path('calendar/', views.CalendarRedirect, name='calendar1'),

    #path('calendar/', views.redirect_calendar, name='calendar'),

    #maybe write as regular def?
    # path to calendar takes in year and month
    path('calendar/<int:year>/<int:month>/', views.CalendarView, name='calendar'),
    #re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),

]
