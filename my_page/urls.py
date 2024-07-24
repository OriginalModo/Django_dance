
from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', include('horoscope.urls')),

    # path('horoscope/leo/', views.leo),
    # re_path(r'', include('horoscope.urls')),
    path('horoscope/', include('horoscope.urls')),
    path('todo_week/', include('weekdays.urls')),
    path('calculate_geometry/', include('geometry.urls')),

]

