from django import forms
from .models import Announcement

class Announcement(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title','body']