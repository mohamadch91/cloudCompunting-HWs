
from dataclasses import fields
from rest_framework import serializers
from .models import *

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
class AddAdvertismentSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    image = serializers.ImageField()
 