from collections import OrderedDict

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import AbstractBaseUser
from rest_framework import serializers

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "user_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, clean_data: dict) -> AbstractBaseUser:
        password = clean_data.pop("password", None)
        instance = self.Meta.model(**clean_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data: dict[str, str]) -> AbstractBaseUser:
        user = authenticate(email=clean_data["email"], password=clean_data["password"])
        if not user:
            raise serializers.ValidationError("user not found")
        return user

    def to_representation(self, instance: OrderedDict) -> OrderedDict:
        ret: OrderedDict = super().to_representation(instance)
        ret.pop("password", None)
        return ret


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username")
