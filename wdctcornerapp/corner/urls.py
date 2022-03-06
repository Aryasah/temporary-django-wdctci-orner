
from django.urls import path
from django.contrib import admin
from . import views
from corner import views
# from django.conf.urls import url,include
urlpatterns = [
    path("", views.index, name='corner'),
    path("gallery", views.home, name='home'),
    # path("", views.contact, name='contact'), 

]