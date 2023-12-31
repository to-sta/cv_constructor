"""
Factories for Tests
"""
import random

import factory
from django.utils import timezone

from authentication.models import UserModel as User

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


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    user_name = factory.Faker("name")
    email = factory.Faker("email")
    password = factory.Faker("password")


class PersonalInformationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PersonalInformation

    user = factory.SubFactory(UserFactory)
    first_name = factory.LazyAttribute(lambda obj: obj.user.user_name.split()[0])
    last_name = factory.LazyAttribute(lambda obj: obj.user.user_name.split()[1])
    date_of_birth = factory.Faker("date_object")
    email = factory.Faker("email")
    phone = factory.Faker("phone_number")
    website = factory.Faker("domain_name")
    image = factory.Faker("image_url")


class WorkExperienceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WorkExperience

    user = factory.SubFactory(UserFactory)
    company = factory.Faker("company")
    location = factory.Faker("city")
    state = random.choice(["CA", "FL", "HI", "NY"])
    job_titel = factory.Faker("job")
    summary = factory.Faker("paragraph")
    start_date = factory.Faker("date_object")
    end_date = factory.Faker("date_object")


class AcademicExperienceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AcademicExperience

    user = factory.SubFactory(UserFactory)
    institution = random.choice(
        [
            "Massachusetts Institute of Technology",
            "California Polytechnic State University",
            "Yale University",
        ]
    )
    location = factory.Faker("city")
    state = random.choice(["CA", "FL", "HI", "NY"])
    degree = random.choice(["bachelor", "master"])
    grade = random.uniform(1, 3)  # There are no bad grades on a resume
    start_date = factory.Faker("date_object")
    end_date = factory.Faker("date_object")
    summary = factory.Faker("paragraph")


class SkillFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Skill

    user = factory.SubFactory(UserFactory)
    skill = random.choice(["Python", "Javascript", "React", "Vue", "C++", "Django"])
    rating = random.randint(1, 5)


class InterestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Interest

    user = factory.SubFactory(UserFactory)
    interest = random.choice(["football", "Basketball", "Yoga", "Reading", "Blogginb"])


class ReferenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reference

    user = factory.SubFactory(UserFactory)
    name = factory.LazyAttribute(lambda obj: obj.user.user_name)
    job_titel = factory.Faker("job")
    company = factory.Faker("company")
    phone = factory.Faker("phone_number")


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Language

    user = factory.SubFactory(UserFactory)
    language = factory.Faker("language_name")
    rating = random.randint(1, 5)


class CurriculumVitaeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CurriculumVitae

    user = factory.SubFactory(UserFactory)
    personal_information = factory.SubFactory(PersonalInformationFactory)
    work_experience = factory.SubFactory(WorkExperienceFactory)
    skill = factory.SubFactory(SkillFactory)
    interest = factory.SubFactory(InterestFactory)
    reference = factory.SubFactory(ReferenceFactory)
    language = factory.SubFactory(LanguageFactory)
    creation_date = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    last_updated = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
