# transect/urls.py
from django.urls import path

from transect.views import index, observation, transect


urlpatterns = [
    path('', index, name='index'),
    path("observation/<int:obvs_id>/", observation, name='observation'),
    path("transect/<int:transect_id>/", transect, name='transect'),
]
