"""URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf.urls import url
from .views import CaseList, CaseDetail

urlpatterns = [
    url(r'^$', CaseList.as_view(), name='case-archive'),
    url(r'^(?P<slug>[-\w]+)/$', CaseDetail.as_view(), name='case-detail')
]
