from django.db import models
from django.urls import reverse
from django.db.models import signals
from django.dispatch import receiver
from django.contrib import admin


# Create your models here.
RESULT_POSSIBILITIES = (
    ('Win','WIN'),
    ('Loss','LOSS'),
    ('Draw','DRAW'),
    ('No Result','NO RESULT'),
)

ROLE_POSSIBILITIES = (
    ('Batsmen','BATSMAN'),
    ('Bowler','BOWLER'),
    ('All Rounder','ALL ROUNDER'),
)

class Venues(models.Model):
    venue_id = models.PositiveIntegerField(unique=True)
    stadium_name = models.CharField(max_length=32,unique=True)
    location = models.CharField(max_length=256)

    def  __str__ (self):
        return self.stadium_name

    def get_absolute_url(self):
        return reverse('venue_list',kwargs={'pk':self.pk})



class Matches(models.Model):
    match_id = models.PositiveIntegerField()
    opponent_name = models.CharField(max_length=128)
    match_date = models.DateField()
    result = models.CharField(max_length=32, choices=RESULT_POSSIBILITIES, default='no_result', null=False)
    match_venue = models.ForeignKey(Venues,related_name='venues',on_delete=models.CASCADE,default="venue name")

    def __str__(self):
        return self.opponent_name

    def get_absolute_url(self):
        return reverse('matches_list',kwargs={'pk':self.pk})

class Player(models.Model):
    player_id = models.PositiveIntegerField()
    player_name = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    role = models.CharField(max_length=32, choices=ROLE_POSSIBILITIES, null=False)
    nationality = models.CharField(max_length=128)

    def __str__(self):
        return self.player_name

    def get_absolute_url(self):
        return reverse('player_list',kwargs={'pk':self.pk})

class Batsman(models.Model):
    batsman_id = models.PositiveIntegerField()
    batsman_name = models.ForeignKey(Player,related_name='batsmanname',on_delete=models.CASCADE)
    real_name = models.CharField(max_length=128,default='c')
    no_matches = models.PositiveIntegerField(default=0)
    total_runs = models.PositiveIntegerField(default=0)
    total_balls = models.PositiveIntegerField(default=0)
    average = models.FloatField(default=0.0)
    strike_rate = models.FloatField(default=0.0)
    fifties = models.PositiveIntegerField(default=0)
    hundreds = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.real_name

    def get_absolute_url(self):
        return reverse('batsman_list',kwargs={'pk':self.pk})

@receiver(signals.pre_save, sender=Batsman)
def update_other_fields(sender, instance, **kwargs):
    if instance.average == 0:
        instance.average = ((instance.total_runs)/(instance.no_matches))
        instance.strike_rate = ((instance.total_runs)/(instance.total_balls)*100)

class Bowler(models.Model):
    bowler_id = models.PositiveIntegerField()
    bowler_name = models.ForeignKey(Player,related_name='bowlername',on_delete=models.CASCADE)
    real_name = models.CharField(max_length=128,default='c')
    no_matches = models.PositiveIntegerField(default=0)
    total_runs = models.PositiveIntegerField(default=0)
    total_balls = models.PositiveIntegerField(default=0)
    total_wickets = models.PositiveIntegerField(default=0)
    average = models.FloatField(default=0.0)
    economy = models.FloatField(default=0.0)
    fourhauls = models.PositiveIntegerField(default=0)
    fivehauls = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.real_name

    def get_absolute_url(self):
        return reverse('bowler_list',kwargs={'pk':self.pk})

@receiver(signals.pre_save, sender=Bowler)
def update_other_fields(sender, instance, **kwargs):
    if instance.average==0:
        instance.average = ((instance.total_runs)/(instance.total_wickets))
        instance.economy = ((instance.total_runs)/((instance.total_balls)/6.0))

class Auction(models.Model):
    auction_id = models.PositiveIntegerField()
    player_name = models.ForeignKey(Player,related_name='auction_player_name',on_delete=models.CASCADE)
    bought_price = models.PositiveIntegerField(default=0)
    sold_price = models.PositiveIntegerField(default=0)
    player_status = models.CharField(max_length=128,default="Status")

    def __str__(self):
        return str(self.player_name)

    def get_absolute_url(self):
        return reverse('auction_list',kwargs={'pk':self.pk})

@receiver(signals.pre_save, sender=Auction)
def update_other_fields(sender, instance, **kwargs):
    if instance.sold_price == 0:
        instance.player_status = "Active Player"
    else:
        instance.player_status = "Ex Player"