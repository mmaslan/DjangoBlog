from django.test import TestCase


class URLTest(TestCase):
    def test_login(self):
        response = self.client.get('/login.html')
        self.assertEqual(response.status_code, 404)

    def test_logout(self):
        response = self.client.get('/logout.html')
        self.assertEqual(response.status_code, 404)

    def test_reset(self):
        response = self.client.get('/password_reset.html')
        self.assertEqual(response.status_code, 404)

    def test_reset_com(self):
        response = self.client.get('/password_reset_complete.html')
        self.assertEqual(response.status_code, 404)

    def test_reset_confirm(self):
        response = self.client.get('/password_reset_confirm.html')
        self.assertEqual(response.status_code, 404)
