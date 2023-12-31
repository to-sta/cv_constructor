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

    def create(self, request: Request) -> Response:
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)

    def update(self, request: Request, pk=None) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request: Request, pk=None) -> Response:
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


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
