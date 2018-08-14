from django.conf import settings
from django.db import models

class Job(models.Model):
  company = models.TextField()
  position = models.TextField()
  location = models.TextField()
  description = models.TextField()
  start_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  company_image = models.CharField(default='/static/images/company/', max_length=500, null=True, blank=True)