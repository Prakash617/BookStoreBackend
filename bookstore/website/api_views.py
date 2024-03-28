from dashboard.models import *
from website.serializers import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class MenusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer
    permission_classes = [AllowAny]

class FaqsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faqs.objects.all()
    serializer_class = FaqsSerializer
    permission_classes = [AllowAny]


class CarousalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Carousal.objects.all()
    serializer_class = CarousalSerializer
    permission_classes = [AllowAny]

class CareersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer
    permission_classes = [AllowAny]