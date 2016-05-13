"""URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^learn/', include('web.urls')),
]
