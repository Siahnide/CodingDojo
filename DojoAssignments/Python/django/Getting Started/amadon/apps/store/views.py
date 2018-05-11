# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse

def index(request):
    del request.session
    lists = []
    items = ["hat","Shirt","jacket","bat"]
    prices = [1.23,2.77,3.99,4.45]
    for x in range(0,len(items)):
        lists.append(items[x])
    request.session["items"] = lists
    lists = []
    for x in range(0,len(prices)):
        lists.append(prices[x])
    request.session["prices"] = lists
    lists = []
    for x in range(0,len(items)):
        lists.append("<div id='item'> <form action='process' method='POST'>{% csrf_token %} <input type='number' name='quantity'></form> </div>")
    request.session["quantity"] = lists
    lists = []

    for x in range(0,len(items)):
        lists.append("<div id='item'> <form action='process' method='POST'>{% csrf_token %} <input type='submit' value='Buy'></form> </div>")
    request.session["buy"] = lists

    return render(request,"store/index.html")

def process(request):
    request.session["activeitem"] = request.POST["hidden"]
    active = request.session["activeitem"]
    
    try: 
        request.session["activequantity"] = int(request.POST["quantity"])
    except:
        context = {"phrase":"Sorry, you must buy at ~Least~ one item."}
        return render(request,"store/index.html",context)
    print request.session["activequantity"]
    
    for x in range(0,len(request.session["items"])):
        if request.session["items"][x] == active:
            request.session["activeprice"] = request.session["prices"][x] * request.session["activequantity"]
            pass
    return redirect('/buy')
def buy(request):
    return render (request,"store/buy.html")
# Create your views here.
