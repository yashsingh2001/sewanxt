from django.db import models

class Homepage(models.Model):
    homepage_username = models.CharField(max_length=50)
    homepage_password = models.CharField(max_length=50)
