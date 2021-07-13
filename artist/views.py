from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import Artist, Album, Song
from .forms import ArtistForm, AlbumForm, SongForm, UserRegistrationForm, LoginForm, SignUpFormEmail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User


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


def signup(request):
    if request.method == 'POST':
        form = SignUpFormEmail(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('artist/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpFormEmail()
    return render(request, 'artist/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')
