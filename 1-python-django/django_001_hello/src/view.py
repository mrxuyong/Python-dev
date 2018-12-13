# -*- coding: UTF-8 -*-

# @author: xuyong

# @file: view.py

# @time: 2018/12/11 下午4:26

# @desc:

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello django ! ")
