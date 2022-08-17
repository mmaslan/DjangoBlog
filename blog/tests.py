from django.test import TestCase


class URLTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/home.html')
        self.assertEqual(response.status_code, 404)

    def test_user_post_list(self):
        response = self.client.get('/user_posts.html')
        self.assertEqual(response.status_code, 404)

    def test_post_details(self):
        response = self.client.get('/post-details.html')
        self.assertEqual(response.status_code, 404)

    def test_post_form(self):
        response = self.client.get('/post-form.html')
        self.assertEqual(response.status_code, 404)

    def test_about(self):
        response = self.client.get('/about.html')
        self.assertEqual(response.status_code, 404)
