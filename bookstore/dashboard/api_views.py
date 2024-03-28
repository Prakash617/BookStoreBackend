from product.serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework.response import Response
from product.models import *
from user_accounts.serializers import CustomUserListSerializer
from website.models import *
from website.serializers import *
from user_accounts.models import *


class DashboardCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = BookCatagoriesSerializer
    permission_classes =[IsAdminUser]

class DashboardSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = BookSubCatagoriesSerializer
    permission_classes =[IsAdminUser]

class DashboardAuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]

class DashboardCouponViewSet(viewsets.ModelViewSet):
    queryset=Coupon.objects.all()
    serializer_class=CouponSerializer
    permission_classes = [IsAdminUser]

class DashboardBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAdminUser]

class DashboardProductQueriesViewSet(viewsets.ModelViewSet):
    queryset=ProductQueries.objects.all()
    serializer_class=ProductQueriesSerializer
    permission_classes =[IsAdminUser]
    
class DashboardProductReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes =[IsAdminUser]

class DashboardCustomUserList(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomUserListSerializer
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()

class DashboardMenusViewSet(viewsets.ModelViewSet):
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer

class DashboardFaqsViewSet(viewsets.ModelViewSet):
    queryset = Faqs.objects.all()
    serializer_class = FaqsSerializer

class DashboardCarousalViewSet(viewsets.ModelViewSet):
    queryset = Carousal.objects.all()
    serializer_class = CarousalSerializer

class DashboardCareersViewSet(viewsets.ModelViewSet):
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer