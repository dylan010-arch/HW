from django.shortcuts import render
import logging

logger = logging.getLogger(_name_)

def book_list(request):
    books = Book.objects.all()
    logger.info (f"Получено {len(books)} книг")
    return render(request, 'books.html', {'books': books})