from django.db import models

# Create your models here.
class Uses(models.Model):
    uses_title = models.CharField(max_length=30)
    uses_des = models.CharField(max_length=500)
class Formdata(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=8)