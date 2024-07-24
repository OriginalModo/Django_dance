from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass

signs = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}


def get_my_date_converter(request, sign_zodiac):
    return HttpResponse(f'<h1>Дата {sign_zodiac}</h1>')


def get_yyyy_converter(request, sign_zodiac):
    return HttpResponse(f'<h1>Число из 4-х цифр {sign_zodiac}</h1>')


def get_my_float_converter(request, sign_zodiac):
    return HttpResponse(f'<h1>Вещественное число {sign_zodiac}</h1>')


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}'


def get_info_sign_horoscope(requests, sign_zodiac: str):
    description = signs.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'my_int': 100,
        'my_float': 100.00,
        'my_list': [1, 2, 3],
        'my_tuple': (1, 2, 3),
        'my_dict': {'name': 'Jack', 'age': 40},
        'my_class': Person('Ji', 1000),
    }
    return render(requests, 'horoscope/info_zodiac.html', context=data)


def main_page(request):
    return HttpResponse('Main Page')


def get_info_sign_horoscope_by_number(requests, sign_zodiac: int):
    zodiacks = list(signs)
    try:
        name_zodiack = zodiacks[sign_zodiac - 1]
        redirect_url = reverse('horoscope_name', args=(name_zodiack,))
        return HttpResponseRedirect(redirect_url)
        # return redirect('https://www.python.org')
    except:
        return HttpResponseNotFound(f'<h1>Знака зодиака {sign_zodiac} не существует</h1>')


def index(request):
    zodiacks = list(signs)
    li_elements = ''
    for i in zodiacks:
        redirect_path = reverse('horoscope_name', args=(i,))
        li_elements += f"<li> <a href='{redirect_path}'>{i.title()}</a> </li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)
