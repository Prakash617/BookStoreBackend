from django.urls import include, path

from website.api_views import *
from bookstore.urls import router

router.register(r'website/carousals',CarousalViewSet,basename='carousals')
router.register(r'website/menus',MenusViewSet,basename='menus')
router.register(r'website/careers',CareersViewSet,basename='careers')
router.register(r'website/faqs',FaqsViewSet, basename='faqs')




urlpatterns = [
    path('api/', include(router.urls)),
   
]