from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse_lazy



def get_rectangle_area(request, height: int, weight: int):
    return HttpResponse(f'<h1>Площадь прямоугольника размером {height}x{weight} равна {height * weight}</h1>')


def get_square_area(request, square: int):
    return HttpResponse(f'<h1>Площадь квадрата размером {square}x{square} равна {square * square}</h1>')


def get_circle_area(request, circle: int):
    def area(radius):
        return __import__("math").pi * (radius ** 2)

    return HttpResponse(f'<h1>Площадь круга радиуса {circle} равна {area(circle):.1f}</h1>')


def get_rectangle_area_redirect(request, height: int, weight: int):
    return redirect(reverse_lazy('rect', args=[height, weight]))


def get_square_area_redirect(request, square: int):
    return redirect(reverse_lazy('squa', args=[square]))


def get_circle_area_redirect(request, circle: int):
    return redirect(reverse_lazy('circ', args=[circle]))


def get_rectangle_area_new(request):
    return render(request, 'geometry/rectangle.html')


def get_square_area_new(request):
    return render(request, 'geometry/square.html')


def get_circle_area_new(request):
    return render(request, 'geometry/circle.html')




















