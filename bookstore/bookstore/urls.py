
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    
)
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('dashboard/',include('dashboard.api_urls')),
    path('product/', include('product.api_urls')),
    # path('website/',include('website.api_urls')),
    # path('users/',include('user_accounts.api_urls')),
    # path('payment/',include('payment.api_urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # ------------------jwt------------
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)