from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import Artist, Album, Song
from .forms import ArtistForm, AlbumForm, SongForm, UserRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def home(request):

    artists = Artist.objects.all()

    return render(request, 'artist/home.html', {'artists':artists})


def detail(request, artist_id):
    
    artist = Artist.objects.get(pk=artist_id)
    albums = artist.albums.all()
   
    return render(request, 'artist/detail.html', {'artist':artist, 'albums':albums})


@login_required(login_url='loginuser')
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

@login_required(login_url='loginuser')
def addartist(request):

    if request.method == "POST":
        form = ArtistForm(request.POST or None, request.FILES or None) 

        if form.is_valid():
            form.save()
            return redirect(home) 
    else:
        form = ArtistForm() 
    
    return render(request, "artist/addartist.html", {'form':form}) 


def register(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None) 
           
        if form.is_valid():
            form.save()
            return redirect(success) 
    else:
        form = UserRegistrationForm() 
    
    return render(request, "artist/register.html", {'form':form}) 


def loginuser(request):

    message_error = ''

    if request.method == "POST":
        form = LoginForm(request.POST or None) 
           
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect(home)

            else:
                message_error = "user name or password is invalid"
       
    else:
        form = LoginForm() 
 
    return render(request, "artist/login.html", {'form':form, 'errors': message_error}) 


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect(home)
    

def success(request):
    
    return render(request, 'artist/success.html')
