from rest_framework import serializers

from .models import (
    AcademicExperience,
    CurriculumVitae,
    Intrest,
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
        fields = "__all__"


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = "__all__"


class AcademicExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicExperience
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class IntrestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intrest
        fields = "__all__"


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"
