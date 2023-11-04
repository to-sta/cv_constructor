from typing import Any

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    User,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_superuser(
        self,
        email: str,
        user_name: str,
        first_name: str,
        password: str,
        **other_fields: bool,
    ) -> Any:
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(
        self,
        email: str,
        user_name: str,
        first_name: str,
        password: str,
        **other_fields: bool,
    ) -> Any:
        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user: User = self.model(
            email=email, user_name=user_name, first_name=first_name, **other_fields
        )  # type: ignore[assignment]
        user.set_password(password)
        user.save()
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name", "first_name"]

    def __str__(self) -> str:
        return self.user_name
