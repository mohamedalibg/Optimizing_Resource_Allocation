from rest_framework import serializers
from .models import Engineer

class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = '__all__'

