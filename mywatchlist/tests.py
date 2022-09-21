from django.test import TestCase,Client

# Create your tests here.
class tes(TestCase):
    def test_url_base(self):
        response = Client().get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)

    def test_contoh_app_using_to_do_list_template(self):
        response = Client().get('/mywatchlist/')
        self.assertTemplateUsed(response, 'mywatchlist.html')

    def test_url_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_url_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

    def test_url_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
