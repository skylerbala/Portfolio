from django.shortcuts import render
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

  contact_form = ContactForm(request.POST or None)
  print('afadslkjf')
  if contact_form.is_valid():
    print('BTICDS')
    subject = contact_form.cleaned_data['subject']
    message = 'From: ' + contact_form.cleaned_data['email'] + '\n' + contact_form.cleaned_data['message']
    email_from = settings.EMAIL_HOST_USER
    email_to = [settings.EMAIL_HOST_USER]
    #send_mail(subject, message, email_from, email_to)
  
  context = {
    "jobs": jobs,
    "skills": skills,
    "projects": projects,
    "volunteer": volunteer,
    "contacts": contacts,
    "contact_form": contact_form
  }

  return render(request, 'home/index.html', context)

def send_message(request):
  send_mail()
  subject = 'Thank you for registering to our site'
  message = 'Email: ' 
  email_from = settings.EMAIL_HOST_USER
  recipient_list = ['receiver@gmail.com',]
  send_mail( subject, message, email_from, recipient_list )
  return redirect('redirect to a new page')