"""URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="core/index.html"), name='core-index'),
    url(r'^tags/', include('core.urls.tags')),
    url(r'^cases/', include('cases.urls.cases')),
    url(r'^articles/', include('cases.urls.articles'))
]