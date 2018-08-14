from django.db import models

# Create your models here.
class Volunteer(models.Model):
  organization = models.TextField()
  position = models.TextField()
  location = models.TextField()
  description = models.TextField()
  start_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  company_image = models.CharField(default='/static/images/company/', max_length=500, null=True, blank=True)