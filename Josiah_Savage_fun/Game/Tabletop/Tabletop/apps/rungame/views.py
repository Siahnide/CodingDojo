# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from classes import Fighter,Rogue

def index(request):
    
    content = {
        'phrase':"hey"
    }
    return render (request,'rungame/index.html',content)


def choose(request):
    content = {
        "phrase":"Thankyou!"
    }
    number = int(request.POST["players"])
    players = []
    for x in range(0,number):
        players.append("Player {}".format(x+1))
    content["players"] = players
    x=0
    # request.session["active"] = content["players"][x]
    
    request.session["totalplayers"] = len(content["players"])
    request.session["active"] = 1
    request.session["playersleft"] = len(content["players"])
    request.session["list"] = []
    return render (request,'rungame/choosechar.html',content)
        
def choosechar(request): 
    content = {}
    if request.POST["char"] == "Fighter":
        print request.session["active"],"is a fighter"
        request.session["playersleft"] -= 1
        request.session["active"] += 1
        request.session["Player {}".format(request.session["active"])] = "Fighter"
        x = "Fighter"
        request.session["list"].append(x)
        content["player {}".format(request.session["active"])] = "Fighter"
    print request.session["list"]
    content = {
        "phrase":'Thankyou!',
        "players":len(request.session["list"])
    }
    
    if request.session["playersleft"] < 1:
        return render (request,'rungame/map.html',content)
    else:
        return render (request,'rungame/choosechar.html',content)


    
# Create your views here.
