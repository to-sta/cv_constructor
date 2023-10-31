from rest_framework import viewsets

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
from .serializers import (
    AcademicExperienceSerializer,
    CurriculumVitaeSerializer,
    IntrestSerializer,
    LanguageSerializer,
    PersonalInformationSerializer,
    ReferenceSerializer,
    SkillSerializer,
    WorkExperienceSerializer,
)


class CurriculumVitaeViewSet(viewsets.ModelViewSet):
    queryset = CurriculumVitae.objects.all()
    serializer_class = CurriculumVitaeSerializer


class PersonalInformationViewSet(viewsets.ModelViewSet):
    queryset = PersonalInformation.objects.all()
    serializer_class = PersonalInformationSerializer


class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class AcademicExperienceViewSet(viewsets.ModelViewSet):
    queryset = AcademicExperience.objects.all()
    serializer_class = AcademicExperienceSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class IntrestViewSet(viewsets.ModelViewSet):
    queryset = Intrest.objects.all()
    serializer_class = IntrestSerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
