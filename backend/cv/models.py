from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CurriculumVitae(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    personal_information = models.ForeignKey(
        "PersonalInformation", on_delete=models.PROTECT
    )
    work_experience = models.ForeignKey("WorkExperience", on_delete=models.PROTECT)
    skill = models.ForeignKey("Skill", on_delete=models.PROTECT)
    interest = models.ForeignKey("Interest", on_delete=models.PROTECT)
    reference = models.ForeignKey("Reference", on_delete=models.PROTECT)
    language = models.ForeignKey("Language", on_delete=models.PROTECT)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} | {self.creation_date}, last update: {self.last_updated}"


class PersonalInformation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    date_of_birth = models.DateField(blank=False)
    email = models.EmailField(blank=False)
    phone = PhoneNumberField(blank=False)
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return f"{self.user} | {self.first_name} {self.last_name}"


class WorkExperience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, blank=False)
    location = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)
    job_titel = models.CharField(max_length=50, blank=False)
    summary = models.TextField(max_length=500, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.user} | {self.start_date} -> {self.end_date}: {self.job_titel}"


class AcademicExperience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=False)
    degree = models.CharField(max_length=100, blank=True)
    grade = models.FloatField(blank=True)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=True)
    summary = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.user} | {self.start_date} -> {self.end_date}: {self.institution}"


class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50, blank=False)
    rating = models.PositiveSmallIntegerField(
        blank=False, validators=[MaxValueValidator(5), MinValueValidator(1)], default=1
    )

    def __str__(self) -> str:
        return f"{self.user} | {self.skill}"


class Interest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    interest = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self) -> str:
        return f"{self.user} | {self.interest}"

    class Meta:
        unique_together = [["user", "interest"]]


class Reference(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, unique=True)
    job_titel = models.CharField(max_length=50, blank=False)
    company = models.CharField(max_length=255, blank=False)
    phone = PhoneNumberField()

    def __str__(self) -> str:
        return f"{self.user} | {self.name} - {self.company}"

    class Meta:
        unique_together = [["user", "name"]]


class Language(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.CharField(max_length=50, blank=False, unique=True)
    # Should have choices rather than min and max, but i will keep it like this for now
    rating = models.PositiveSmallIntegerField(
        blank=False, validators=[MaxValueValidator(5), MinValueValidator(1)], default=1
    )

    def __str__(self) -> str:
        return f"{self.user} | {self.language}"

    class Meta:
        unique_together = [["user", "language"]]
