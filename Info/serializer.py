from rest_framework import serializers
from .models import Reports


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['email','name']
