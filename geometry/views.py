from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound


def get_rectangle_area(request, height: int, weight: int):
    return HttpResponse(f'<h1>Площадь прямоугольника размером {height}x{weight} равна {height * weight}</h1>')


def get_square_area(request, square: int):
    return HttpResponse(f'<h1>Площадь квадрата размером {square}x{square} равна {square * square}</h1>')


def get_circle_area(request, circle: int):
    def area(radius):
        return __import__("math").pi * (radius ** 2)

    return HttpResponse(f'<h1>Площадь круга радиуса {circle} равна {area(circle):.1f}</h1>')
