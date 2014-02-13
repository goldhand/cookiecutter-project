# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import BlogView


urlpatterns = patterns('blog.views',
    url(r'^$',
        BlogView.as_view(template_name='blog/list.html'),
        name="list"),
    )