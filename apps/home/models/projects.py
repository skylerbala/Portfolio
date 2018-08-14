from django.db import models

class Project(models.Model):
  name = models.TextField()
  description = models.TextField()
  position = models.TextField()
  start_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  project_image = models.CharField(default='/static/images/personal/', max_length=500, null=True, blank=True)
  link = models.URLField(null=True, blank=True)
  
  