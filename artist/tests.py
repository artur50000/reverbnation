from django.test import TestCase
from django.urls import reverse
from .models import Artist, Album
from django.contrib.auth.models import User
from .forms import ArtistForm, AlbumForm, SongForm, UserRegistrationForm, LoginForm, SignUpFormEmail

# Create your tests here.

class ArtistViewTest(TestCase):

   # model tests
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testingpass12345')
        self.artist = Artist.objects.create(user=self.user, name="Bob Dilan", bio="no bio")
        self.artist.save()


    def test_artist(self):
        artist = Artist.objects.get(id=self.artist.id)
        self.assertEqual(artist.name, "Bob Dilan")

        
    def test_album(self):
        artist = Artist.objects.get(id=self.artist.id)
        album = Album.objects.create(artist=self.artist, title="neverland", year="2021-02-01")
        album.save()
        self.assertEqual(album.title, "neverland")


    def test_field(self):
        a_length = len(self.artist.name)
        self.assertTrue(a_length < 80)


    #forms tests
    def test_registerform(self):
        username = "test123"
        email = "email@mail.ru"
        password1 = "passwwddff11"
        password2 = "ddwwddssaafd11"
        form = UserRegistrationForm(data={'username':username, 'email':email, 'password1':password1, 'password2':password2})
        self.assertFalse(form.is_valid())


    def test_registerform2(self):
        username = "test123"
        email = "email@mail.ru"
        password1 = "passwwddff11"
        password2 = "passwwddff11"
        form = UserRegistrationForm(data={'username':username, 'email':email, 'password1':password1, 'password2':password2})
        self.assertTrue(form.is_valid())


    #url tests
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/artist/')
        self.assertEqual(response.status_code, 200)

    
    def test_view_url_exists_at_desired_location_second(self):
        response = self.client.get('/artist/addartist')
        self.assertEqual(response.status_code, 302)


    def test_view_url_exists_at_desired_location_third(self):
        response = self.client.get('/artist/addalbum')
        self.assertRedirects(response, '/artist/loginuser?next=/artist/addalbum')


    def test_view_url_exists_at_desired_location_fourth(self):
        response = self.client.get('/artist/login')
        self.assertEqual(response.status_code, 200)


    def test_view_url_exists_at_desired_location_fourth(self):
        response = self.client.get('/artist/register')
        self.assertEqual(response.status_code, 200)


    def test_contain_text(self):
        response = self.client.get('/artist/register')
        self.assertContains(response, 'Create an Account') 
        self.assertContains(response, '<form method="POST" class="form-group">')
    