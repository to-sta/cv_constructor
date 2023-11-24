import pytest
from .factory import (
    CurriculumVitaeFactory,
    PersonalInformationFactory,
    WorkExperienceFactory,
    AcademicExperienceFactory,
    SkillFactory,
    LanguageFactory,
    InterestFactory,
    ReferenceFactory,
)


def test_str_methods() -> None:
    cv = CurriculumVitaeFactory.build()
    personal_information = PersonalInformationFactory.build()
    work_experience = WorkExperienceFactory.build()
    academic_experience = AcademicExperienceFactory.build()
    skill = SkillFactory.build()
    interest = InterestFactory.build()
    reference = ReferenceFactory.build()



    language = LanguageFactory.build()
    interest = InterestFactory.build()
    reference = ReferenceFactory.build()
    assert str(cv) == f"{cv.user} | {cv.creation_date}, last update: {cv.last_updated}"
    assert (
        str(personal_information)
        == f"{personal_information.user} | {personal_information.first_name} {personal_information.last_name}"
    )
    assert (
        str(work_experience)
        == f"{work_experience.user} | {work_experience.start_date} -> {work_experience.end_date}: {work_experience.job_titel}"
    )
    assert (
        str(academic_experience)
        == f"{academic_experience.user} | {academic_experience.start_date} -> {academic_experience.end_date}: {academic_experience.institution}"
    )
    assert str(skill) == f"{skill.user} | {skill.skill}"
    assert str(interest) == f"{interest.user} | {interest.interest}"
    assert str(reference) == f"{reference.user} | {reference.name} - {reference.company}"
    assert str(language) == f"{language.user} | {language.language}"
