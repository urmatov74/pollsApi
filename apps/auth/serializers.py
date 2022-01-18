from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def validate(self, args):
        username = args.get('username', None)
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'Такой логин занят'})
        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')
