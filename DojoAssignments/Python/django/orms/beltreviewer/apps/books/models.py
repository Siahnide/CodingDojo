# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render,redirect,HttpResponse




class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author',related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)
    

class Author(models.Model):
    name = models.CharField(max_length=255)

class Review(models.Model):
    content = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    book = models.ForeignKey('book',related_name="book")

    created_at = models.DateTimeField(auto_now_add=True)
    



class Process(models.Manager):
    status = True
    def double(self,request):
        request.session["error"] = ""
        if self.status == True:
            author = Author.objects.all()
            for x in author:
                if x == request.POST["new_author"]:
                    request.session["error"] = "Author already exists"
                    print self.status
                    return self
                else:
                    print self.status
                    return self

    def create(self,request):
        if self.status == True:
            if request.POST["title"] == "":
                self.status == False
                return self
            if request.POST["content"] == "":
                self.status = False
                return self
            if request.POST["new_author"] != "":
                Author.objects.create(name=request.POST["new_author"])
                Book.objects.create(title = request.POST["title"],author = Author.objects.filter(name= request.POST["new_author"])[0])
            if request.POST["new_author"] == "":
                print request.POST["author"]
                Book.objects.create(title = request.POST["title"],author = Author.objects.filter(name= request.POST["author"])[0])
            if request.POST["content"] != "":
                if request.POST["rating"] != "":
                    Review.objects.create(content=request.POST["content"],rating=request.POST["rating"],creator=request.session["active_name"],book=Book.objects.filter(title=request.POST["title"])[0])
                elif request.POST["rating"] == "":
                    del(request.POST["rating"])
                    self.status = False
                    return self
            return self

                    
                





