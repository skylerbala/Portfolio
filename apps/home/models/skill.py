from django.db import models

# Create your models here.


class Skill(models.Model):
  GENERAL = 'GENERAL'
  PROGRAMMING_LANGUAGES = 'Programming Languages'
  FRAMEWORKS_LIBRARIES = 'Frameworks / Libraries'
  LANGUAGES = 'Languages'

  WORKING_KNOWLEDGE = 'Working Knowledge'
  PROFICIENT = 'Proficient'
  ADVANCED = 'Advanced'
  EXPERT = 'Expert'

  PROFICIENCY_LEVELS = (
      (WORKING_KNOWLEDGE, 'Working Knowledge'),
      (PROFICIENT, 'Proficient'),
      (ADVANCED, 'Advanced'),
      (EXPERT, 'Expert'),
  )

  SKILL_TYPES = (
      (GENERAL, 'General'),
      (PROGRAMMING_LANGUAGES, 'Programming Languages'),
      (FRAMEWORKS_LIBRARIES, 'Frameworks / Libraries'),
      (LANGUAGES, 'Languages'),
  )

  skill_type = models.TextField(choices=SKILL_TYPES, default=PROGRAMMING_LANGUAGES)
  name = models.TextField()
  icon = models.CharField(default='/static/images/skills/', max_length=500, null=True, blank=True)
  proficiency = models.TextField(choices=PROFICIENCY_LEVELS, default=PROFICIENT)
  