from rest_framework import serializers
from .models import Account


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
