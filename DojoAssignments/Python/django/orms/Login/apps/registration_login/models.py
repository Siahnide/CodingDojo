# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponse
import re,bcrypt
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Validate(models.Manager):
    status = True
    def check(self,request):
        request.session["error"] = ["","","","",""]
        try:
            if len(request.POST["first_name"]) <2:
                self.status = False
                request.session["error"][0] = "\n Incorrect First Name field"
        except:pass
        try:
            if len(request.POST["last_name"]) <2:
                self.status = False
                request.session["error"][1] = "\n Incorrect Last Name field"
        except:pass
        try:
            if request.POST["email"] == "":
                self.status = False
                request.session["error"][2] = "\n Incorrect Email field"
        except:pass
        try:
            if not EMAIL_REGEX.match(request.POST['email']):
                self.status = False
                request.session["error"][2] = "\n Incorrect Email field"
        except:pass
        try:
            if len(request.POST["password"]) <8:
                self.status = False
                request.session["error"][3] = "\n Incorrect Password field"
                del(request.session["error"][4])
        except:pass
        try:
            if request.POST["confirm"] != request.POST["password"] :
                self.status = False
                try:request.session["error"][4] = "\n Passwords Do not match"
                except:pass
                del(request.session["error"][3])
        except:pass
        return self
    def save(self,request):
        if self.status == True:
            password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],email=request.POST["email"],password=password)
            return self
            
        else:
            self.status = False
            return self




    def login(self,request):
        user = User.objects.filter(email=request.POST["email"])[0]
        print user.first_name
        password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
        print password
        if bcrypt.checkpw(request.POST["password"].encode(), user.password.encode()) == True:
            print "TRUE"
            return self
        else:
            request.session["error"][0] = "Incorrect Password/Email"
            self.status = False
            return self




class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


# Create your models here.
