from rest_framework import serializers
from rest_framework.authentication import get_user_model
from .models import Fath, Kid


class LoginSer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField()


class RegisterSer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        username, password, confirm_password, email = attrs['username'], attrs['password'], attrs['confirm_password'], attrs['email']
        if get_user_model().objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists')
        if password != confirm_password:
            raise serializers.ValidationError('Password OkDone')
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return get_user_model().objects.create_user(**validated_data)
    

class FathSer(serializers.ModelSerializer):
    class Meta:
        model = Fath
        fields=['name', 'age']
        read_only_fields=['created_at', 'updated_at']


class KidSer(serializers.ModelSerializer):
    class Meta:
        model = Kid
        fields=['name', 'age', 'father']
        read_only_fields=['created_at', 'updated_at']
    


