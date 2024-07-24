
from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    # re_path(r'<sign_zodiac>', get_info_about_sign_zodiac),
    path(r'rectangle/<int:height>/<int:weight>', get_rectangle_area, name='rect'),
    path(r'square/<int:square>', get_square_area, name='squa'),
    path(r'circle/<int:circle>', get_circle_area, name='circ'),

    path(r'rectangle/<int:height>/<int:weight>/', get_rectangle_area),
    path(r'square/<int:square>/', get_square_area),
    path(r'circle/<int:circle>/', get_circle_area),

    path(r'get_rectangle_area/<int:height>/<int:weight>/', get_rectangle_area_redirect),
    path(r'get_square_area/<int:square>/', get_square_area_redirect),
    path(r'get_circle_area/<int:circle>/', get_circle_area_redirect),

    re_path(r'get_rectangle_area/[Aa]+', get_rectangle_area_new),
    re_path(r'get_square_area/[Aa]+', get_square_area_new),
    re_path(r'get_circle_area/[Aa]+', get_circle_area_new),


]
