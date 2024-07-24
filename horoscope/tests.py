from django.test import TestCase
from horoscope.views import signs

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
        list_of_zodiacs = list(signs)
        for i, v in enumerate(list_of_zodiacs, start=1):
            response = self.client.get(f'/{i}')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{v}/')


    def test_signs(self):
        zodiacs = signs
        for i in zodiacs:
            response = self.client.get(f'/horoscope/{i}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                signs[i],
                response.content.decode()
            )









