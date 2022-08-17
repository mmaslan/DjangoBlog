from django.test import TestCase


class URLTest(TestCase):
    def test_login(self):
        response = self.client.get('/users/login.html')
        self.assertTrue(response)

    def test_logout(self):
        response = self.client.get('/logout.html')
        self.assertTrue(response)

    def test_reset(self):
        response = self.client.get('/password_reset.html')
        self.assertTrue(response)

    def test_reset_com(self):
        response = self.client.get('/password_reset_complete.html')
        self.assertTrue(response)

    def test_reset_confirm(self):
        response = self.client.get('/password_reset_confirm.html')
        self.assertTrue(response)
