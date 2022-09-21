from django.test import TestCase, Client

# Create your tests here.
class appexist(TestCase):
    def test_contoh_app_url_exists(self):
        response = Client().get('/katalog/')
        self.assertEqual(response.status_code, 200)