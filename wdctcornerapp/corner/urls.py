
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from corner import views
# from django.conf.urls import url,include
urlpatterns = [
    path("", views.index, name='corner'),
    path("gallery", views.home, name='home'),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)