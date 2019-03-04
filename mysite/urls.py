"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.urls import path
from cmdb import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.temp),
    url(r'^index/', views.index),
    url(r'^forms/', views.forms, name='forms'),
    url(r'^temp/', views.temp, name='temp'),
    # url(r'^login/', views.login, name='login'),
    url(r'^login/', views.login, name='login'),
    url(r'^registered/', views.registered, name='registered'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^audio_test/', views.audio_test, name='audio_test'),
    url(r'^xx/', views.xx, name='xx'),
    url(r'^ajax_patient$', views.ajax_patient),
    url(r'^ajax_patient_info$', views.ajax_patient_info),
    url(r'^ajax_report_detail$', views.ajax_report_detail),
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'^run_py$', views.run_py, name='run_py'),
    url(r'^insert_into_mysql$', views.insert_into_mysql, name='insert_into_mysql'),

    # path('admin/', admin.site.urls),
]
