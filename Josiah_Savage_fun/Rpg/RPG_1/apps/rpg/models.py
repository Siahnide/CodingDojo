# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render,redirect,HttpResponse


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    name = models.CharField(max_length=255)
    hp = models.IntegerField(default=0)
    ac = models.IntegerField(default=0)
    dmg = models.IntegerField(default=0)
    atk = models.IntegerField(default=0)
    sp = models.IntegerField(default=0)
    ranged = models.IntegerField(default=0)
    slot = models.CharField(max_length=255,default="none")

class Char(models.Model):
    name = models.CharField(max_length=255)
    hp = models.IntegerField(default=15)
    ac = models.IntegerField(default=10)
    sp = models.IntegerField(default=30)
    dmg = models.IntegerField(default=1)
    atk = models.IntegerField(default=0)
    ranged = models.IntegerField(default=0)
    head_item = models.ForeignKey(Item,related_name="head", default=Item.objects.filter(name="none")[0].id)
    chest_item = models.ForeignKey(Item,related_name="chest", default=Item.objects.filter(name="none")[0].id)
    arms_item = models.ForeignKey(Item,related_name="arms", default=Item.objects.filter(name="none")[0].id)
    feet_item = models.ForeignKey(Item,related_name="feet", default=Item.objects.filter(name="none")[0].id)
    right_hand_item = models.ForeignKey(Item,related_name="right_hand", default=Item.objects.filter(name="none")[0].id)
    left_hand_item = models.ForeignKey(Item,related_name="left_hand", default=Item.objects.filter(name="none")[0].id)
    






    



# Create your models here.
