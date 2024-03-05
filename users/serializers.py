from rest_framework import serializers 
from .models import CustomUser



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create (self, validated_data ):
        password = validated_data.get('password' , None)
        instance = self.Meta.model(**validated_data)
        if password is not None :
            instance.set_password(password )
        instance.save()
        return instance
            
        
