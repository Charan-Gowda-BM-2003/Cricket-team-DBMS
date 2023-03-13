from django.urls import path
from . import views

urlpatterns = [
    path('matches/',views.MatchesDetailView,name='MatchesDetailView'),
    path('player/',views.PlayerDetailView,name='PlayerDetailView'),
    path('batsman/',views.BatsmanDetailView,name='BatsmanDetailView'),
    path('bowler/',views.BowlerDetailView,name='BowlerDetailView'),
    path('auction/',views.AuctionDetailView,name='AuctionDetailView'),
    path('venues/',views.VenuesDetailView,name='VenuesDetailView'),
    path('sp1/',views.PlayerBatsmenForm,name='PlayerBatsmenForm'),
    path('sp2/',views.PlayerBowlerForm,name='PlayerBowlerForm'),
]