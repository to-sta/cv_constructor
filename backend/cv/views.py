from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

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
from .serializers import (
    AcademicExperienceSerializer,
    CurriculumVitaeSerializer,
    InterestSerializer,
    LanguageSerializer,
    PersonalInformationSerializer,
    ReferenceSerializer,
    SkillSerializer,
    WorkExperienceSerializer,
)


class CurriculumVitaeViewSet(viewsets.ModelViewSet):
    queryset = CurriculumVitae.objects.all()
    serializer_class = CurriculumVitaeSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)


class PersonalInformationViewSet(viewsets.ModelViewSet):
    queryset = PersonalInformation.objects.all()
    serializer_class = PersonalInformationSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)


class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)


class AcademicExperienceViewSet(viewsets.ModelViewSet):
    queryset = AcademicExperience.objects.all()
    serializer_class = AcademicExperienceSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)


class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)
