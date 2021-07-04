from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class ArtistViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/artist/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location_second(self):
        response = self.client.get('/artist/addartist')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location_third(self):
        response = self.client.get('/artist/addalbum')
        self.assertEqual(response.status_code, 200)


    