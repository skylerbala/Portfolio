from django.contrib import admin
from .models.contacts import Contact
from .models.jobs import Job
from .models.projects import Project
from .models.skills import Skill
from .models.volunteer import Volunteer


admin.site.register(Volunteer)

admin.site.register(Skill)

admin.site.register(Project)

admin.site.register(Contact)

admin.site.register(Job)
