# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=1000)
    course = models.ForeignKey(Course,related_name="comment")


# Create your models here.
