from django.contrib import admin
from .models import Venues, Matches, Player, Batsman, Bowler, Auction

# Register your models here.
admin.site.register(Venues)
admin.site.register(Matches)
admin.site.register(Player)
admin.site.register(Batsman)
admin.site.register(Bowler)
admin.site.register(Auction)