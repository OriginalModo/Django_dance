
from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    # re_path(r'<sign_zodiac>', get_info_about_sign_zodiac),
    path(r'rectangle/<int:height>/<int:weight>', get_rectangle_area),
    path(r'square/<int:square>', get_square_area),
    path(r'circle/<int:circle>', get_circle_area),
    path(r'rectangle/<int:height>/<int:weight>/', get_rectangle_area),
    path(r'square/<int:square>/', get_square_area),
    path(r'circle/<int:circle>/', get_circle_area),



]
