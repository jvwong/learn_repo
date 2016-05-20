"""URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf.urls import url, include
from core.views.tags import TaggedArticleList, TaggedCaseList

urlpatterns = [
    url(r'^articles/(?P<tag>[-\w]+)/$', TaggedArticleList.as_view(), name="article-tag-list"),
    url(r'^cases/(?P<tag>[-\w]+)/$', TaggedCaseList.as_view(), name="case-tag-list")
]