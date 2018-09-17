from django.db import models

class Project(models.Model):
  name = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  project_image_1 = models.CharField(default='/static/images/projects/', max_length=500, null=True, blank=True)
  project_image_2 = models.CharField(default='/static/images/projects/', max_length=500, null=True, blank=True)
  link = models.URLField(null=True, blank=True)
  
  