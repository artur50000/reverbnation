from django.forms import ModelForm
from .models import Artist, Album, Song

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
