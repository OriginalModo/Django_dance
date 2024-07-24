
from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    # re_path(r'<sign_zodiac>', get_info_about_sign_zodiac),
    path(r'<int:sign_zodiac>', get_info_sign_horoscope_by_number),
    path(r'<int:sign_zodiac>/', get_info_sign_horoscope_by_number),
    path(r'<str:sign_zodiac>', get_info_sign_horoscope),
    path(r'<str:sign_zodiac>/', get_info_sign_horoscope),

    # re_path(r'^leo/', leo),
    # re_path(r'^scorpio/', scorpio),
    # re_path(r'^aries/', aries),
    # re_path(r'^taurus/', taurus),

]
