from django.urls import include, path

from dashboard.api_views import *
from bookstore.urls import router

router.register(r'dashboard/dashboard_categories',DashboardCategoryViewSet,basename='dashboard_categories')
router.register(r'dashboard/dashboard_subcategories',DashboardSubCategoryViewSet,basename='dashboard_subcategories')
router.register(r'dashboard/dashboard_author',DashboardAuthorViewSet,basename='dashboard_author')
router.register(r'dashboard/dashboard_book',DashboardBookViewSet,basename='dashboard_book')
router.register(r'dashboard/dashboard_queries',DashboardProductQueriesViewSet,basename='dashboard_queries')
router.register(r'dashboard/dashboard_review',DashboardProductReviewViewSet,basename='dashboard_review')
router.register(r'dashboard/coupons',DashboardCouponViewSet,basename='dashboard_coupon')
router.register(r'dashboard/user_list',DashboardCustomUserList,basename='user_list')
router.register(r'dashboard/dashboard_carousals',DashboardCarousalViewSet,basename='dashboard_carousals')
router.register(r'dashboard/dashboard_menus',DashboardMenusViewSet,basename='dashboard_menus')
router.register(r'dashboard/dashboard_careers',DashboardCareersViewSet,basename='dashboard_careers')
router.register(r'dashboard/dashboard_faqs',DashboardFaqsViewSet, basename='dashboard_faqs')




urlpatterns = [
    path('api/', include(router.urls)),
   
]