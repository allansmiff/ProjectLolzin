from django.urls import path
from . import views


#class that defines the urls that the application can use
urlpatterns = [
    path('summoner', views.summoner_form),
    path('summonerView', views.summoner_view),
]
