from django.contrib.auth.models import User
from django import forms
from .models import Song

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username','email','password']

class SongAddForm(forms.ModelForm):
	
	class Meta:
		model = Song
		fields = ['song_title','file_type','is_favorite']