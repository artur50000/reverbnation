from django.forms import ModelForm
from .models import Artist, Album, Song
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['user','name', 'bio', 'image']

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
