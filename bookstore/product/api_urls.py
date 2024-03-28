from django.urls import include, path

from product.api_views import *
from bookstore.urls import router

router.register(r'book/categories',CategoryViewSet,basename='catogories')
router.register(r'book/subcategories',SubCategoryViewSet,basename='subcategories')
router.register(r'book/author',AuthorViewSet,basename='author')
router.register(r'book/books',BookViewSet,basename='book')
router.register(r'book/queries',ProductQueriesViewSet,basename='book_queries')
router.register(r'book/review',ProductReviewViewSet,basename='book_review')
router.register(r'coupon/coupons',CouponViewSet,basename='book_coupon')
router.register(r'book/used_book',UsedBookViewSet,basename='used_book')
router.register(r'book/new_arrival',NewArrivalBookViewSet,basename='new_arrival')
router.register(r'book/nepali_book',NepaliBookViewSet,basename='nepali_book')
router.register(r'book/best_seller',BestSellerBookViewSet,basename='best_seller')
router.register(r'book/author_book',AuthorBookViewSet,basename='author_book') #?author_name





urlpatterns = [
    path('api/', include(router.urls)),
   
]