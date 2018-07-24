# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from models import *


def index(request):
    request.session["active_name"] = ""
    return render(request,'registration_login/index.html')

def register(request):
    if Validate().check(request).save(request).status == True:
        context = {"user":User.objects.filter(email=request.POST["email"])[0]}
        request.session["active_name"] = context["user"].first_name
        return redirect('/books/redirect')
    else:
        return redirect('/')
    
def login(request):
    if Validate().check(request).status == True:
        if Validate().login(request).status == True:
            context = {"user":User.objects.filter(email=request.POST["email"])[0]}
            request.session["active_name"] = context["user"].first_name
            return redirect('/books/redirect')
        else:
            return redirect('/')
    else:
        print "FALSE"
        return redirect('/')

    
# Create your views here.
