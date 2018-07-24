# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from ..rpg.models import *
from ..rpg.Sim import *
from models import *


def desert(request):
    context = {
        "active":Char.objects.filter(name=request.session["active"])[0]
    }
    return render(request,'game/desert.html',context)
# Create your views here.
