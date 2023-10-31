from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "cv"

router = DefaultRouter()
router.register(r"curriculum_vitae", views.CurriculumVitaeViewSet)
router.register(r"personal_information", views.PersonalInformationViewSet)
router.register(r"work_experience", views.WorkExperienceViewSet)
router.register(r"academic_experience", views.AcademicExperienceViewSet)
router.register(r"skill", views.SkillViewSet)
router.register(r"intrest", views.IntrestViewSet)
router.register(r"reference", views.ReferenceViewSet)
router.register(r"language", views.LanguageViewSet)


urlpatterns = [
    path("", include(router.urls)),
]