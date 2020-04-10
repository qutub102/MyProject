from django.conf.urls import url,include
from django.contrib import admin
from home import views

urlpatterns = [
    url('index',views.index,name='home'),
    url('about',views.about,name='about'),
    url('service',views.service,name='service'),
    url('contact',views.contact,name='contact'),
    url('login',views.loginUser,name='login'),
    url('signup',views.signup,name='signup'),
    url('customer',views.customer,name='customer'),
    url('logout',views.logoutUser,name="logoutUser")
]
