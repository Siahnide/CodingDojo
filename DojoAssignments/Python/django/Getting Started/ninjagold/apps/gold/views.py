# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
import random

def index(request):
    response = "hi"
    request.session["yourgold"] = 0
    request.session["stuff"] = ""
    return render(request,"gold/index.html")


def process(request):
    if request.method == "POST":
        if request.POST["findgold"] =='farm':
            goldtemp = random.randrange(10,21)
            request.session['yourgold'] += goldtemp
            print goldtemp
            string = "<div id='green'>Earned " + str(goldtemp) + " gold from the " + str(request.POST["findgold"]) + "!<br></div>"
            request.session['stuff'] += str(string)
            return render(request,"gold/index.html")

        elif request.POST["findgold"] =='cave':
            goldtemp = random.randrange(5,11)
            request.session['yourgold'] += goldtemp
            string = "<div id='green'>Earned " + str(goldtemp) + " gold from the " + str(request.POST["findgold"]) + "!<br></div>"
            request.session['stuff'] += str(string)
            return render(request,"gold/index.html")

        elif request.POST["findgold"] =='house':
            goldtemp = random.randrange(2,6)
            request.session['yourgold'] += goldtemp
            string = "<div id='green'>Earned " + str(goldtemp) + " gold from the " + str(request.POST["findgold"]) + "!<br></div>"
            request.session['stuff'] += str(string)
            return render(request,"gold/index.html")

        elif request.POST["findgold"] =='casino':
            goldtemp = random.randrange(0,51)
            take = random.randrange(1,3)
            print take
            if take == 1:
                request.session['yourgold'] += goldtemp
                string = "<div id='green'>Earned " + str(goldtemp) + " gold from the " + str(request.POST["findgold"]) + "!<br></div>"
            if take ==2:
                request.session['yourgold'] -= goldtemp
                string = "<div id='red'>Lost " + str(goldtemp) + " gold from the " + str(request.POST["findgold"]) + "... Ouch...<br></div>"
            request.session['stuff'] += str(string)
            return render(request,"gold/index.html")

        elif request.POST["findgold"] =='empty':
            request.session['yourgold'] = 0
            request.session['stuff'] = ""
            return render(request,"gold/index.html")
    else:
        return redirect ('/gold')
    


# Create your views here.
