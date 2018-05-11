# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.utils.crypto import get_random_string

    
def index(request):
    if request.method == "POST":
        request.session["times"] += 1
    elif request.method == "GET":
        request.session["times"] = 0
    times = request.session["times"]    
    content ={
        'word':get_random_string(length=20),
    }
    return render (request,'words/index.html',content)




# Create your views here.
