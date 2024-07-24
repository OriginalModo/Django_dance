from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy, reverse

dct = {
    'monday': 'в понедельник я жалею себя',
    'tuesday': 'во вторник - глазею в пропасть',
    'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
    'thursday': 'в четверг - зарядка',
    'friday': 'ужин с собой, нельзя снова его пропускать',
    'saturday': 'в субботу - борьба с презрением к себе',
    'sunday': 'в воскресенье - иду на рождество',
}

def monday(request, day):
    try:
        return HttpResponse(f'<h1>{dct[day]}</h1>')
    except:
        return HttpResponseNotFound(f'<h1>{day} не существует</h1>')


def monday_int(request, day):
    days = list(dct)
    day_dct = days[day - 1]
    redirect_url = reverse('day_day', args=(day_dct,))
    match day:
        case x if day in range(1, 8):
            return redirect(redirect_url)
        case _:
            return HttpResponseNotFound(f'<h1>Неверный номер дня - {day}</h1>')

def hH(request):
    return render(request, 'weekdays/greeting.html')

























