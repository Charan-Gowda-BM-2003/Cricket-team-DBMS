from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from .models import Venues, Matches, Player, Batsman, Bowler, Auction

# Create your views here.
class IndexView(TemplateView):
    template_name = 'teamapp/index.html'

def MatchesDetailView(request):
    allmatches = Matches.objects.all()
    context_dict = {'allmatches':allmatches}
    return render(request,'teamapp/matches_list.html',context_dict)

def PlayerDetailView(request):
    allplayer = Player.objects.all()
    context_dict = {'allplayer':allplayer}
    return render(request,'teamapp/player_list.html',context_dict)

def BatsmanDetailView(request):
    allbatter = Batsman.objects.all()
    context_dict = {'allbatter':allbatter}
    return render(request,'teamapp/batsman_list.html',context_dict)

def BowlerDetailView(request):
    allbowler = Bowler.objects.all()
    context_dict = {'allbowler':allbowler}
    return render(request,'teamapp/bowler_list.html',context_dict)

def AuctionDetailView(request):
    allauctions = Auction.objects.all()
    context_dict = {'allauctions':allauctions}
    return render(request,'teamapp/auction_list.html',context_dict)

def VenuesDetailView(request):
    allvenues = Venues.objects.all()
    context_dict = {'allvenues':allvenues}
    return render(request,'teamapp/venue_list.html',context_dict)

def PlayerBatsmenForm(request):
    form = forms.PlayerBatsmen
    allplayer = Player.objects.all()
    allbatter = Batsman.objects.all()

    if request.method == 'POST':
        form = forms.PlayerBatsmen(request.POST)

        if form.is_valid():
            print(form.cleaned_data['Name'])
            return render(request,'teamapp/plrbat2.html',{'form':form.cleaned_data['Name'],'allplayer':allplayer,'allbatter':allbatter})

    return render(request,'teamapp/plrbat.html',{'form':form,'allplayer':allplayer,'allbatter':allbatter})

def PlayerBowlerForm(request):
    form = forms.PlayerBowler
    allplayer = Player.objects.all()
    allbowler = Bowler.objects.all()

    if request.method == 'POST':
        form = forms.PlayerBowler(request.POST)

        if form.is_valid():
            print(form.cleaned_data['Name'])
            return render(request,'teamapp/plrblr2.html',{'form':form.cleaned_data['Name'],'allplayer':allplayer,'allbowler':allbowler})

    return render(request,'teamapp/plrblr.html',{'form':form,'allplayer':allplayer,'allbowler':allbowler})