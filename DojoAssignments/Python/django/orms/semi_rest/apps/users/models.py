# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponse

from django.db import models

class Validate(models.Manager):
    def check(self,request):
        if request.method=="POST":
            print "GOT POST"
            if request.POST["name"] == "":
                request.session["err"] += "Must include a name"
                return redirect('/')
            if request.POST["email"] == "":
                request.session["err"] += "Must include an email"
                return redirect('/')
            else:
                return True
    def create(self,request):
        User.objects.create(name=request.POST["name"],email=request.POST["email"])
        return self
    def update(self,request,ids):
        user = User.objects.get(id=ids)
        user.name = request.POST["name"]
        user.email = request.POST["email"]
        user.save()

class User (models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)





# Create your models here.
