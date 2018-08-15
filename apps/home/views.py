from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models.jobs import Job
from .models.skills import Skill
from .models.projects import Project
from .models.volunteer import Volunteer
from .models.contacts import Contact
from .forms import ContactForm

def index(request):
  jobs = Job.objects.all()
  skills = Skill.objects.all()
  projects = Project.objects.all()
  volunteer = Volunteer.objects.all()
  contacts = Contact.objects.all()
  contact_form = ContactForm
  
  context = {
    "jobs": jobs,
    "skills": skills,
    "projects": projects,
    "volunteer": volunteer,
    "contacts": contacts,
    "contact_form": contact_form
  }

  return render(request, 'home/index.html', context)