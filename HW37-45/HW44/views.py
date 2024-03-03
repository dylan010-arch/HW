from rest_framework import viewsets
from .models import Book
from .permissions import Isadminreadonly

class MyModelViewSet (viewsets.ModelViewSet):
    queryset = Book.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return DefaultSerializer
        if self.action == 'retrieve':
            return BookDetailSerializer
        return DefaultSerializer # Замените на ваш базовый класс стерилизатор