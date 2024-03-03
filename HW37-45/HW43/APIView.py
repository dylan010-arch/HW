from rest_framework.views import APIView
from rest_framework.response import Response

class MyView(APIView) :
    def get (self, request):
        # логика для GET запроса
        return Response({'message': 'Hello for GET'})
    
    def post (self, request) :
        # логика для POST запроса
        return Response({'message': 'Hello for POST'})