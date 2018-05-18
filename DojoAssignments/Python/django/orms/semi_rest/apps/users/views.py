# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from models import *


def index(request):
    
    return render(request,'users/index.html')



def show(request):
    context = {"User":User.objects.all()}
    print User.objects.all()
    return render(request,'users/show.html',context)

def process(request):
    request.session["err"] = ""
    if request.method=="POST":
        Validate().check(request)
    if Validate().check(request) == True:
        Validate().create(request)
        redirect('/show')
    return redirect('/show')

def processids(request,ids):
    request.session["err"] = ""
    if request.POST["name"] == "":
        return redirect('/edit/{}'.format(ids))
    if request.POST["email"] == "":
        return redirect('/edit/{}'.format(ids))
    Validate().update(request,ids)
    return redirect('/show')
def edit(request,ids):
    context = {"User":User.objects.get(id=ids)}
    return render(request,"users/edit.html",context)

def delete(request,ids):
    user = User.objects.get(id=ids)
    user.delete()
    return redirect('/show')

def user(request,ids):
    context = {"User":User.objects.get(id=ids)}
    return render(request,'users/user.html',context)


# Create your views here.
