from rest_framework import serializers

from authentication.models import UserModel


class RegisterNewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("email", "user_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> UserModel:
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
