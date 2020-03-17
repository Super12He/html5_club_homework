from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^forms/$', views.forms, name='forms'),
    url(r'^base/$', views.base, name='base'),
    url(r'^blank/$', views.blank, name='blank'),
    url(r'^report/([0-9]+)', views.reports, name='report'),
    url(r'^report/$', views.reports, name='report'),
]
