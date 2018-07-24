from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render,redirect,HttpResponse
from models import *


class Sim(models.Manager):
    status = True
    def create(self,request):

        if request.method == "POST":
            Char.objects.create(
                name=request.POST["name"],
                head_item=Item.objects.filter(slot="head",name=request.POST["head"])[0],
                chest_item=Item.objects.filter(slot="chest",name=request.POST["chest"])[0],
                arms_item=Item.objects.filter(slot="arms",name=request.POST["arms"])[0],
                feet_item=Item.objects.filter(slot="feet",name=request.POST["feet"])[0],
                left_hand_item=Item.objects.filter(slot="left_hand",name=request.POST["left_hand"])[0],
                right_hand_item=Item.objects.filter(slot="right_hand",name=request.POST["right_hand"])[0],
                )
            character = Char.objects.filter(name=request.POST["name"])[0]
            items =[
                Item.objects.filter(slot="head",name=request.POST["head"])[0],
                Item.objects.filter(slot="chest",name=request.POST["chest"])[0],
                Item.objects.filter(slot="arms",name=request.POST["arms"])[0],
                Item.objects.filter(slot="feet",name=request.POST["feet"])[0],
                Item.objects.filter(slot="left_hand",name=request.POST["left_hand"])[0],
                Item.objects.filter(slot="right_hand",name=request.POST["right_hand"])[0],
            ]
            
            for x in items:
                character.hp  += x.hp
                character.ac += x.ac
                character.atk += x.atk
                character.dmg += x.dmg
                character.sp += x.sp
                character.ranged + x.ranged
                character.save()    

            request.session["active"] = character.name

        
        return redirect('/character')
        return self