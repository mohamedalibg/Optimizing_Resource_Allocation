from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)  # Add profile_picture to handle file upload

    class Meta:
        model = CustomUser
        fields = ['id','username', 'password', 'first_name', 'last_name', 'email', 'profile_picture', 'date_joined', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        profile_picture = validated_data.pop('profile_picture', None)  # Get profile_picture if present
        
        user = CustomUser(**validated_data)
        
        if password:
            user.set_password(password)
        
        user.save()
        
        if profile_picture:
            user.profile_picture = profile_picture
            user.save()
        
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        profile_picture = validated_data.pop('profile_picture', None)  # Get profile_picture if present

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()

        if profile_picture:
            instance.profile_picture = profile_picture
            instance.save()
        
        return instance
