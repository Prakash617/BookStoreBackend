from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = BookCatagoriesSerializer
    permission_classes =[AllowAny]

class SubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = BookSubCatagoriesSerializer
    permission_classes =[AllowAny]

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class CouponViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Coupon.objects.all()
    serializer_class=CouponSerializer
    permission_classes = [AllowAny]

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[AllowAny]

class UsedBookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Book.objects.filter(is_used=True)
        return queryset

class BestSellerBookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes =[AllowAny]
    
    def get_queryset(self):
        queryset = Book.objects.filter(top_selling=True)
        return queryset

class NewArrivalBookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes =[AllowAny]
    
    def get_queryset(self):
        queryset = Book.objects.filter(new_arrival=True)
        return queryset

class NepaliBookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes =[AllowAny]
    
    def get_queryset(self):
        queryset = Book.objects.filter(language="Nepali")
        return queryset

class AuthorBookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def list(self, request):
        author_name = request.query_params.get('author_name')
        print("hello",author_name)
        if author_name:
            books = Book.objects.filter(authors__name__icontains=author_name)
            serializer = self.serializer_class(books, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No data"}, status=200)



class ProductQueriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=ProductQueries.objects.all()
    serializer_class=ProductQueriesSerializer
    
class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer