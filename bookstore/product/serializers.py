from rest_framework import serializers
from .models import *



class BookCatagoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
        

        
class BookSerializer(serializers.ModelSerializer):
    book_category = BookCatagoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = "__all__"