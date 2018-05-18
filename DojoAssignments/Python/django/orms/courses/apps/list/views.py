# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from models import *

def index(request):
    context={"Course":Course.objects.all()}
    return render(request,'list/index.html',context)


def process(request):
    if request.method == "POST":
        if len(request.POST["name"]) > 5:
            if len(request.POST["description"]) > 14:
                Course.objects.create(name=request.POST["name"],description=request.POST["description"])
                return redirect('/')
            else:
                return redirect('/')
        else:
            return redirect('/')


def remove(request,ids):
    print ids
    course = Course.objects.get(id=ids)
    course.delete()
    return redirect('/')

def read(request,ids):
    context={"Course":Course.objects.get(id=ids)}
    return render(request,'list/read.html',context)


def comment(request,ids):
    if request.method=="POST":
        try:Comment.objects.create(content=request.POST["content"],course=Course.objects.get(id=ids))
        except:pass
        
    context={
        "Course":Course.objects.get(id=ids),
        "Comment":Comment.objects.filter(course=ids),
    }
    print context["Comment"]
    return render(request,'list/comments.html',context)

def really(request,ids):
    context={"Course":Course.objects.get(id=ids)}
    return render(request,'list/really.html',context)
# Create your views here.
