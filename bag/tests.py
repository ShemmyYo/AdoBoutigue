from django.test import TestCase


class TestViews(TestCase):
    def test_basket_view(self):
        """
        Testing if the User can access products page
        """
        resp = self.client.get('/bag/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'bag/bag.html')
