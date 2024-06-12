from django.db import models

class Homesignup(models.Model):
    homesignup_username = models.CharField(max_length=50)
    homesignup_password = models.CharField(max_length=50)
    homesignup_email = models.EmailField()