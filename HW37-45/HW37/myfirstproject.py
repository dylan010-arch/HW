# myfirstproject/views.py
from django.http import HttpResponse

def get_example (request) :
# Получаем значение параметра 'name' из GET запроса
    name = request.GET.get('name', 'Гость')
    return HttpResponse (f"Привет, {name}!")