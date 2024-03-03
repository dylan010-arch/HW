from django.http import HttpResponse

def home(request):
    return HttpResponse("Приветствую на странице")

def about(request):
    return HttpResponse("О нас")

def current_datetime(request):
    pass

def greet(request, name):
    return HttpResponse(f"Привет, {name}!")
