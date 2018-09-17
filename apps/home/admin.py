from django.contrib import admin
from .models.contact import Contact
from .models.job import Job
from .models.project import Project
from .models.skill import Skill
from .models.volunteer import Volunteer


admin.site.register(Volunteer)

admin.site.register(Skill)

admin.site.register(Project)

admin.site.register(Contact)

admin.site.register(Job)
