# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from home.models import Contact,Signup
# Register your models here.
admin.site.register(Contact)
admin.site.register(Signup)