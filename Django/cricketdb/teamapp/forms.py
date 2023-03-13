from django import forms
from .models import Player,Batsman,Bowler

class PlayerBatsmen(forms.Form):
    Name = forms.CharField(max_length=64)

    def clean_Name(self):
        Name = self.cleaned_data['Name']
        return Name

class PlayerBowler(forms.Form):
    Name = forms.CharField(max_length=64)

    def clean_Name(self):
        Name = self.cleaned_data['Name']
        return Name