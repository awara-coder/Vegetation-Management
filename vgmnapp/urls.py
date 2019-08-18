from vgmnapp import views
from vgmnapp.views import *
from django.urls import path
urlpatterns = [
path('get_colleges/', basic_view.as_view(), name="colleges"),
path('get_detect', detect_view.as_view(), name="apple"),
path('get_weather', weather_view.as_view(), name="banana"),
        ]
