from rest_framework import serializers
from .models import *



class BookCatagoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BookSubCatagoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model= Coupon
        fields= '__all__'
        

class ProductQueriesSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductQueries
        fields= '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields= '__all__'



        
class BookSerializer(serializers.ModelSerializer):
    book_category = BookCatagoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = "__all__"