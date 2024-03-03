from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Главная страница',
        'description': 'Это описание главной страницы.'
    }
    return render(request, 'home.html', context)
