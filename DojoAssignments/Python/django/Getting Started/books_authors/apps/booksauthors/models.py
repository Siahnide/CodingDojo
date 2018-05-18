# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(Authors,related_name="books")
# Create your models here.


How does a heart lack if no one has noticed it's presence and where does it go? 
YOU HAVE SET YOUR HEART ON HAUNTING ME FOREVER FROM THE START ITS NEVER SILENT