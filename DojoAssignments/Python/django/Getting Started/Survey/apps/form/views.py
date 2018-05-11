# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from time import gmtime, strftime


def index(request):
    content={
        "phrase":"hello"
    }
    return render(request,"form/index.html",content)


def process(request):
    request.session["fullname"] = request.POST["fullname"]
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]
    request.session["comment"] = request.POST["comment"]
    
    
    return redirect ('/card')
    
def card(request):
    return render(request,"form/card.html")
# Create your views here.
