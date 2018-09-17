from django.conf import settings
from django.db import models

class Job(models.Model):
  company = models.TextField(null=True, blank=True)
  position = models.TextField(null=True, blank=True)
  location = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  start_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  company_image = models.CharField(default='/static/images/jobs/', max_length=500, null=True, blank=True)