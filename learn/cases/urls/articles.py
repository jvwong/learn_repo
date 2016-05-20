"""URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf.urls import url
from cases.views import ArticleList, ArticleDetail

urlpatterns = [
    url(r'^$', ArticleList.as_view(), name='article-list'),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetail.as_view(), name='article-detail')
]
