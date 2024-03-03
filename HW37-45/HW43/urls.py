from django.utils import path
from .views import MyView

urlpatterns = [
    path('myview/', MyView.as_view()),
]