from django.shortcuts import render
from .models import Artist, Album, Song
from .forms import ArtistForm, AlbumForm, SongForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    artists = Artist.objects.all()

    return render(request, 'artist/home.html', {'artists':artists})

def detail(request, artist_id):
    
    artist = Artist.objects.get(pk=artist_id)
    #albums = Album.objects.filter(artist=artist_id)
    albums = artist.albums.all()
    #songs = Song.objects.filter(album=album.id)
    

    return render(request, 'artist/detail.html', {'artist':artist, 'albums':albums})

def addalbum(request):

    if request.method == "POST":

        if request.POST.get("form_type") == 'formOne':

            form = AlbumForm(request.POST or None, request.FILES or None) 
            form_two = SongForm() 

            if form.is_valid():
                form.save()
                return redirect(home) 
        elif request.POST.get("form_type") == 'formTwo': 
            form_two = SongForm(request.POST or None, request.FILES or None)
            form = AlbumForm()  

            if form_two.is_valid():
                form_two.save()
                return redirect(home) 

    else:
        form = AlbumForm() 
        form_two = SongForm() 
    
    return render(request, "artist/addalbum.html", {'form':form, 'form_two':form_two}) 


def addartist(request):

    if request.method == "POST":
        form = ArtistForm(request.POST or None, request.FILES or None) 

        if form.is_valid():
            form.save()
            return redirect(home) 
    else:
        form = ArtistForm() 
    
    return render(request, "artist/addartist.html", {'form':form}) 
