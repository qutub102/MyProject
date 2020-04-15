# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    about=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name

class Signup(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=50)
    date=models.DateField()

    def __str__(self):
        return self.name

class Service(models.Model):
    food_id=models.AutoField
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    img=models.ImageField(upload_to='shop/')

    def __str__(self):
        return self.name