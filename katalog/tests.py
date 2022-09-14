from django.test import TestCase

# Create your tests here.
class URLtest(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/katalog')
        self.assertEqual(response.status_code, 200)
