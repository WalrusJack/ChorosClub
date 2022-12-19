from django import forms
from .models import Trip, Log, UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ('title', 'description')


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ('title', 'description', 'type', 'trip')
