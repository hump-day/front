# transect/urls.py
from django.urls import path

from transect.views import index, observation, transect, test, api, observations, upload


urlpatterns = [
    path('', index, name='index'),
    path("observations/<int:obvs_id>/", observation, name='observation'),
    path("transect/<int:transect_id>/", transect, name='transect'),
    path("test/", test),
    path("api/", api),
    path("upload", upload),
    path("observations", observations)
]
