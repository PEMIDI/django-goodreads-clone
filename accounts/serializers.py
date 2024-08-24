from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from config.constants import Decision

CustomUser = get_user_model()


class BaseAuthSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class LoginUserSerializer(BaseAuthSerializer):

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = CustomUser.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            raise serializers.ValidationError(
                'Incorrect email or password.'
            )
        return user


class RegisterUserSerializer(BaseAuthSerializer):

    def validate(self, attrs):
        email = attrs.get('email')
        user_exists = CustomUser.objects.filter(email=email).exists()
        if user_exists:
            raise serializers.ValidationError("Email already exists.")
        return attrs

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
