# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from models import *

from Sim import *



def menu(request):
    request.session["active"] = ""
    return render(request,'rpg/menu.html')

def single(request):
    if request.method == "GET":
        
        context = {
            "active":Char.objects.filter(name=request.session["active"])[0],
             }
        print Char.objects.filter(name=request.session["active"]).values_list()[0][2:]
        print Char.objects.filter(name=request.session["active"]).values()[0]
        return render(request,'rpg/singleplayer_menu.html',context)
    context = {}
    return render(request,'rpg/singleplayer_menu.html',context)

def item(request):
    context={"Item":Item.objects.all()}
    return render(request,'rpg/item.html',context)


def add_item(request):
    Item.objects.create(name=request.POST["name"],hp=request.POST["hp"],ac=request.POST["ac"],dmg=request.POST["dmg"],atk=request.POST["atk"],sp=request.POST["sp"],slot=request.POST["slot"],ranged=request.POST["ranged"],)
    return redirect('/item')

def create_char(request):
    if request.method == "POST":
        Sim().create(request)
        return redirect('/single')
    else:
        context = {
            "item":[
                Item.objects.filter(slot="head"),
                Item.objects.filter(slot="chest"),
                Item.objects.filter(slot="arms"),
                Item.objects.filter(slot="feet"),
                Item.objects.filter(slot="right_hand"),
                Item.objects.filter(slot="left_hand"),
                ]
            }
    return render(request,'rpg/create_char.html',context)
    
def load_char(request):
    context = {"char":Char.objects.all()}
    if request.method == "POST":
        request.session["active"] = request.POST["name"]
        return redirect('/single')

    return render(request,'rpg/load_char.html',context)

def del_char(request):
    char = Char.objects.filter(name=request.POST["name"])[0]
    char.delete()
    return redirect('/load_char')







# Create your views here.
