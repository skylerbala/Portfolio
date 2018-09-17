from django.db import models

class Contact(models.Model):
  email = models.EmailField()
  phone = models.CharField(max_length=10)
  github_url = models.URLField()
  linkedin_url = models.URLField()