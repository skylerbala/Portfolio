from django.db import models

# Create your models here.
class Volunteer(models.Model):
  organization = models.TextField(null=True, blank=True)
  position = models.TextField(null=True, blank=True)
  location = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  start_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  company_image = models.CharField(default='/static/images/company/', max_length=500, null=True, blank=True)