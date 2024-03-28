from django.urls import include, path

from order.api_views import *
from bookstore.urls import router

router.register(r'order/guest_checkout',GuestOrderViewSet,basename='guest_checkout')
router.register(r'order/return',OrderRejectedViewSet,basename='return')
router.register(r'order/cancel',OrderCancelledViewSet,basename='cancel')
router.register(r'order/track_myorder',OrdersTrackingViewSet,basename='track_myorder')





urlpatterns = [
    path('api/', include(router.urls)),
   
]