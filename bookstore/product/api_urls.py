from django.urls import include, path

from product.api_views import *
from bookstore.urls import router

router.register(r'product/categories',CategoryViewSet,basename='catogeries')
router.register(r'product/products',BookViewSet,basename='product')



urlpatterns = [
    path('api/', include(router.urls)),
   
]