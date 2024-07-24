from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def monday(request, day):
    dct = {
        'monday': 'в понедельник я жалею себя',
        'tuesday': 'во вторник - глазею в пропасть',
        'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
        'thursday': 'в четверг - зарядка',
        'friday': 'ужин с собой, нельзя снова его пропускать',
        'saturday': 'в субботу - борьба с презрением к себе',
        'sunday': 'в воскресенье - иду на рождество',
    }
    try:
        return HttpResponse(f'<h1>{dct[day]}</h1>')
    except:
        return HttpResponseNotFound(f'<h1>{day} не существует</h1>')


def monday_int(request, day):
    match day:
        case x if day in range(1, 8):
            return HttpResponse(f'Сегодня {day} день недели')
        case _:
            return HttpResponse(f'<h1>Неверный номер дня - {day}</h1>')