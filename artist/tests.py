from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class ArtistViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/artist/')
        self.assertEqual(response.status_code, 200)

    '''
    def test_view_url_exists_at_desired_location_second(self):
        response = self.client.get('/artist/addartist')
        self.assertTrue('login' in response.context)
    '''
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
    