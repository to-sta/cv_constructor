from typing import Any

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import (
    AcademicExperience,
    CurriculumVitae,
    Interest,
    Language,
    PersonalInformation,
    Reference,
    Skill,
    WorkExperience,
)


class CurriculumVitaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumVitae
        fields = "__all__"


class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        exclude = ["user"]


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        exclude = ["user"]


class AcademicExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicExperience
        exclude = ["user"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ["user"]

    def validate(self, attrs: Any) -> Any:
        user = self.context["request"].user
        skill = attrs["skill"]
        rating = attrs["rating"]

        if Skill.objects.filter(user=user, skill=skill, rating=rating).exists():
            raise ValidationError(
                "A record with this user, skill and rating already exists"
            )
        return attrs


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        exclude = ["user"]

    def validate(self, attrs: Any) -> Any:
        user = self.context["request"].user
        interest = attrs["interest"]

        if Skill.objects.filter(user=user, interest=interest).exists():
            raise ValidationError("A record with this user and interest already exists")
        return attrs


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        exclude = ["user"]

    def validate(self, attrs: Any) -> Any:
        user = self.context["request"].user
        name = attrs["name"]

        if Skill.objects.filter(user=user, name=name).exists():
            raise ValidationError("A record with this user and name already exists")
        return attrs


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        exclude = ["user"]

    def validate(self, attrs: Any) -> Any:
        user = self.context["request"].user
        language = attrs["language"]

        if Skill.objects.filter(user=user, language=language).exists():
            raise ValidationError("A record with this user and language already exists")
        return attrs
