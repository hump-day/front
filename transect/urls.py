# transect/urls.py
from django.urls import path

from transect.views import index


urlpatterns = [
    path('', index),
]