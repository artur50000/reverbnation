from django.contrib import admin
from .models import Artist, Album, Song

# Register your models here.


#admin.site.register(Artist)
#admin.site.register(Album)
#admin.site.register(Song)

@admin.register(Album)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['title','artist','year']
    list_filter = ['artist']

@admin.register(Artist)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name','user','image']
    list_filter = ['user']

@admin.register(Song)
class AlbumSong(admin.ModelAdmin):
    list_display = ['album','title', 'album__artist']
    list_filter = ['album']

    @admin.display(description='Artist')
    def album__artist(self, song):
        return song.album.artist.name


