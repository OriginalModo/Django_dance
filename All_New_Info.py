"""

 При запуске  python manage.py runserver
 http://127.0.0.1:8000/ - Означает вашу локальную машину или  localhost
 http://localhost:8000/ - Тоже самое

 # В терминале  вводим  where python
 where python - покажет список всех существующих Интерпретаторов Python.
  Первый в списке тот который запускается. Тот который в списке выше и будет запускатся

 python название_файла.py  - Запуск файла в терминале

 (venv) - Если вначале Терминала стоит строчка  (venv) значит используется Виртуальное Окружение

 Другой кнопкой мышки на проект и выбираем Reload from disk - Обновить папку вручную


 Чтобы выполнять команды нужно Быть в той же папке на том же уровне или используем команду cd

    -- командная строка cmd   Terminal commands --
 dir - Отображение файлов и папок в текущем каталоге
 cd - Изменить каталог, если нажать Tab будет автодополнение
 cd .. - переход на 1 папку назад
 cd ..\.. - переход на 2 папки назад
 cd \ - Переход в корневую директорию
 cd . - Переход в текущую директорию (никаких изменений)


 cd папка\папка\папка   -  Быстрый переход за одну операцию
 cd "имя имя"  - если между именами пробел
 cd "Абсолютный путь" - Сразу перейдем туда куда нужно
 Название_Диска: - чтобы сменить диск  - Примеры C:  D:  Только название диска и двоеточие в терминале(командной строке)

 mkdir - создание папки


  Все команды:    python manage.py --help    или просто  python manage.py
                  django-admin --help        или просто  django-admin
  python manage.py collectstatic -   Проверка статики
  python manage.py makemigrations - Проверка миграции
  python manage.py migrate - Применить миграции
  django-admin startproject - Создание проекта
  python manage.py startapp - Создание приложения
  python manage.py runserver - Запуск сервера для разработки
  python manage.py createsuperuser - Создать аккаунт администратора


 Чтобы запускать несколько серверов прописываем разные порты в  Edit Configurations... runserver 8000   runserver 8001


 --- ПО Поводу добавления приложения в settings.py  INSTALLED_APPS ---
 Ведь автор говорил, что нужно добавлять в settings.py имя добавляемого приложения. Я создал приложение blog и
 НЕ добавил его в INSTALLED_APPS, но всё-равно всё функционирует.

 В большинстве документации просто говорится, что нужно добавить имя каждого приложения в массив INSTALLED_APPS в
 настройках проекта Django. В чем преимущество/цель этого? Какую другую функциональность я получу,
 если создам 2 приложения, но включу в массив INSTALLED_APPS только имя одного?

 Django использует INSTALLED_APPS список всех мест для поиска моделей, команд управления, тестов и других утилит.

 Если вы создали два приложения (скажем, myappи myuninstalledapp), но только одно из них указано в INSTALLED_APPS,
 вы заметите следующее поведение:

 1) Модели, содержащиеся в , myuninstalledapp/models.pyникогда не вызовут изменений миграции (или не сгенерируют
 начальные миграции). Вы также не сможете взаимодействовать с ними на уровне базы данных, поскольку их таблицы никогда не будут созданы.

 2) Статические файлы, перечисленные внутри, myapp/static/будут обнаружены как часть collectstatic или службы
 статических файлов тестового сервера, но myuninstalledapp/staticфайлы не будут обнаружены.

 3) Тесты внутри myapp/tests.pyзапускались, но myuninstalledapp/tests.pyне работали.

 4) Команды управления, перечисленные в, myuninstalledapp/management/commands/не будут обнаружены.

 Так что на самом деле вы можете иметь папки в своем проекте Django, которые не являются установленными приложениями
 (вы даже можете создать их с помощью python manage.py startapp), но просто знайте, что некоторые утилиты
 автоматического обнаружения Django не будут работать для этого приложения.


 Подключить приложение в файле Основного проекта urls.py
  path('horoscope/', include('horoscope.urls')),


 Конвертеры роутов Расположение важно Обработка роутов идет сверху вниз: Динамические url
 path(r'<str:sign_zodiac>/', get_info_sign_horoscope),            # Тип Строка
 path(r'<int:sign_zodiac>', get_info_sign_horoscope_by_number),   # Тип Число



 Располагаются они в модуле django.urls.converters
 DEFAULT_CONVERTERS = {
     'int': IntConverter(),
     'path': PathConverter(),
     'slug': SlugConverter(),
     'str': StringConverter(),
     'uuid': UUIDConverter(),
 }

 Также можно создавать свои собственные конвертеры
 class MyDateConverter:
     regex = '^(0[1-9]|[12][0-9]|3[01])[-](0[1-9]|1[012])[-](19|20)\d\d$'

     def to_python(self, value):
         return datetime.strptime(value, f'%d-%m-%Y')

     def to_url(self, value):
         # return value.strftime(f'%d-%m-%Y')
         return f'{value:%d-%m-%Y}'


 from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, ...

 HttpResponse - возвращает Ответ на Запрос.  статус код - 200
 HttpResponseNotFound - возвращает ошибку 404 и сообщение об ошибке Страница не найдена.  статус код - 404

    try:
        return HttpResponse(f'<h1>{dct[day]}</h1>')
    except:
        return HttpResponseNotFound(f'<h1>{day} не существует</h1>')

 HttpResponseRedirect - Перенаправление пользователя на другую страницу веб-сайта. статус код - 302

 def index(request):
    return HttpResponseRedirect('https://www.python.org')

 Функция redirect - также помогает выполнить перенаправление в Django.  статус код - 302

 from django.shortcuts import redirect

    def index(request):
      return redirect('https://www.python.org')


 Функция reverse - позволяет генерировать URL-адреса на основе имен URL-адресов в вашем приложении.

 from django.urls import reverse        # Тоже самое
 from django.shortcuts import reverse   # Тоже самое

 reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)

 # Передать можно коллекцию
 reverse('my_view', args=[1])
 reverse('my_view', args=(1, ))
 reverse('my_view', kwargs={'slug': 'hello-world'})


 # Имя нашего роута  Имя для URL-адреса
  path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),


 Тестирование unittest в Django

 В Django тесты определяются в специальном модуле tests.py внутри приложения.
 В файлике test пишем тесты

 # Пример
 from django.test import TestCase

 class TestHoroscope(TestCase):

    # Тест на статут кода
    def test_index(self):
        response = self.client.get('/horoscope/')  # client - Замена Браузера
        self.assertEqual(response.status_code, 200)

    # Тест на статут кода и перенаправление
    def test_libra_redirect(self):
        response = self.client.get('/7')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/horoscope/libra/')

 # Затем в терминале пишем команду
 python manage.py test название_приложения

 Типы проверок в классе TestCase
 assertEqual(a, b)          a == b
 assertNotEqual(a, b)       a != b
 assertTrue(x)              bool(x) is True
 assertFalse(x)             bool(x) is False
 assertIs(a, b)             a is b
 assertIsNot(a, b)          a is not b
 assertIsNone(x)            x is None
 assertIsNotNone(x)         x is not None
 assertIn(a, b)             a in b
 assertNotIn(a, b)          a not in b
 assertIsInstance(a, b)     isinstance(a, b)
 assertNotIsInstance(a, b)  not isinstance(a, b)







































































































































































































"""