from django.contrib import admin

from .models import (
    CurriculumVitae,
    Interest,
    Language,
    PersonalInformation,
    Reference,
    Skill,
    WorkExperience,
)

# Register your models here.
admin.site.register(CurriculumVitae)
admin.site.register(PersonalInformation)
admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(Reference)
admin.site.register(Language)
