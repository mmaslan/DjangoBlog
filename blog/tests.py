from django.test import TestCase


class URLTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/home.html')
        self.assertTrue(response)

    def test_user_post_list(self):
        response = self.client.get('/user_posts.html')
        self.assertTrue(response)

    def test_post_details(self):
        response = self.client.get('/post-details.html')
        self.assertTrue(response)

    def test_post_form(self):
        response = self.client.get('/post-form.html')
        self.assertTrue(response)

    def test_about(self):
        response = self.client.get('/about.html')
        self.assertTrue(response)