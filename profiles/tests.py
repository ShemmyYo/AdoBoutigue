from django.test import TestCase
from django.contrib.auth.models import User


class TestingProfiles(TestCase):

    def test_profile(self):
        """
        Test if testuser can access profile
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_logged_out(self):
        """
        Test if logged out user gets redirected
        when trying to access profile link
        """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)