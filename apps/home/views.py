from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from django.http import HttpResponse
from .models.job import Job
from .models.skill import Skill
from .models.project import Project
from .models.volunteer import Volunteer
from .models.contact import Contact
from .forms import ContactForm

class Index(View):
  contact_form = ContactForm
  template_name = 'home/index.html'

  def get(self, request):
    jobs = Job.objects.order_by('start_date').reverse().all()
    skills = Skill.objects.all()
    projects = Project.objects.order_by('start_date').reverse().all()
    volunteer = Volunteer.objects.order_by('start_date').reverse().all()
    contacts = Contact.objects.all()
    
    context = {
      "jobs": jobs,
      "skills": skills,
      "projects": projects,
      "volunteer": volunteer,
      "contacts": contacts,
      "contact_form": self.contact_form
    }

    return render(request, self.template_name, context)
    
  def post(self, request):
    contact_form = self.contact_form(request.POST)
    if contact_form.is_valid():
      subject = contact_form.cleaned_data['subject']
      message = 'From: ' + contact_form.cleaned_data['email'] + '\n' + contact_form.cleaned_data['message']
      email_from = settings.EMAIL_HOST_USER
      email_to = [settings.EMAIL_HOST_USER]
      send_mail(subject, message, email_from, email_to)
      return HttpResponse('Success')