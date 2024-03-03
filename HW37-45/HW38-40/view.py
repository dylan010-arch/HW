from django.shortcuts import render

def products_view(request):
    products = [
        {'name': 'Продукт 1', 'price': 150},
        {'name': 'Продукт 2', 'price': 300},
        {'name': 'Продукт 3', 'price': 450}
    ]
    return render(request, 'products.html', {'products': products})
