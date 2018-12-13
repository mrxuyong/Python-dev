# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: urls.py

# @time: 2018/12/11 下午4:28

# @desc:

from django.conf.urls import url

from . import view

urlpatterns = [
    url(r'^$', view.hello),
]
