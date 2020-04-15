# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from home.models import Contact,Signup,Service
# Register your models here.
admin.site.register(Contact)
admin.site.register(Signup)
admin.site.register(Service)