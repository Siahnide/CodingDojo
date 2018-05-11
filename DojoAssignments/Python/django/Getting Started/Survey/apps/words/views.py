# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from time import gmtime, strftime


def index(request):

    
    

    return render (request,"words/index.html")


def process(request):
    try: 
        
        if len(request.session["list"]) == 0:
            request.session["list"] = []
        else: 
            pass    
    except: 
        request.session["list"] = []
        pass
    
    if request.method=="POST":
        word = request.POST["word"]
        color = request.POST["color"]
        try: size = request.POST["size"]
        except: size = ""
        time =strftime("%Y-%m-%d %H:%M %p", gmtime())
        lists = request.session["list"]
        lists.append( "<div id='{}{}'> {}  {}</div>".format(color,size,word,time) )
        print lists
        request.session["list"] = lists
        print request.session["list"]

        
    return redirect ('/words')

def clear(request):
    try:
        del request.session["list"]
        
    except:pass
    return redirect ('/words')