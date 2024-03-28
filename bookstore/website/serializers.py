from .models import *
from rest_framework import serializers


class CareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = "__all__"

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = "__all__"

class CarousalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousal
        fields = "__all__"

class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = "__all__"