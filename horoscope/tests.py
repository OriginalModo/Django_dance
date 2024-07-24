from django.test import TestCase


class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/libra')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
                      response.content.decode())

    def test_libra_redirect(self):
        response = self.client.get('/7')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/horoscope/libra/')









