
from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path(r'<int:day>', monday_int),
    path(r'<int:day>/', monday_int),

    path(r'<str:day>', monday, name='day_day'),
    path(r'<str:day>/', monday, name='day_day'),



]
