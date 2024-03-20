from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[AllowAny]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = BookCatagoriesSerializer
    permission_classes =[AllowAny]