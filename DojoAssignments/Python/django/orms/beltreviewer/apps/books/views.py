# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse

from models import *

from ..registration_login.models import *

def add(request):
    context={'Book':Book.objects.all()}
    return render(request,'books/add.html',context)

def process(request):
    if Process().create(request).status == True:
        context={'Book':Book.objects.all()}
        return redirect('/books/show')
    else:
        
        return redirect('/books/add')


def delete(request,ids):
    book = Book.objects.filter(id=ids)
    book.delete()
    context={'Book':Book.objects.all()}
    return redirect('/books/show')

def show(request):
    books= Book.objects.all()[:3]
    titles = []
    for x in range(0,3):
        titles.append(Review.objects.all()[len(Review.objects.all())-1-x])
    print titles
    context={'Book':Book.objects.all()[:3],'Review':titles,"Books":Book.objects.all()}

    return render(request,'books/show.html',context)

def user(request,ids):
    reviews= Review.objects.all()
    creators = []
    for x in reviews:
        if x.creator == ids:
            creators.append(x)

    context={'User':User.objects.filter(first_name=ids)[0],"Review":creators}
    
    return render(request,'books/user.html',context)

def book(request,ids):
    context={'Book':Book.objects.filter(id=ids)[0],'Review':Review.objects.filter(book=Book.objects.filter(id=ids))}
    return render(request,'books/book.html',context)

def review(request,ids):
    Review.objects.create(content=request.POST["content"],rating=request.POST["rating"],creator=request.session["active_name"],book=Book.objects.filter(title=request.POST["title"])[0])
    content = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    book = models.ForeignKey('book',related_name="book")

    created_at = models.DateTimeField(auto_now_add=True)
    return redirect('/books/{}'.format(ids))
# Create your views here.
