
from django.contrib import admin
from django.urls import path, re_path, converters, register_converter
from .views import *
from . import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    # re_path(r'<sign_zodiac>', get_info_about_sign_zodiac),
    path('', index, name='main'),
    path(r'<my_date:sign_zodiac>', get_my_date_converter),
    path(r'<yyyy:sign_zodiac>', get_yyyy_converter),
    path(r'<int:sign_zodiac>', get_info_sign_horoscope_by_number),
    path(r'<my_float:sign_zodiac>', get_my_float_converter),
    path(r'<int:sign_zodiac>/', get_info_sign_horoscope_by_number),

    path(r'<str:sign_zodiac>', get_info_sign_horoscope),
    path(r'<str:sign_zodiac>/', get_info_sign_horoscope, name='horoscope_name'),

    # re_path(r'^leo/', leo),
    # re_path(r'^scorpio/', scorpio),
    # re_path(r'^aries/', aries),
    # re_path(r'^taurus/', taurus),

]
