from django.db import models

# Create your models here.
class Uses(models.Model):
    uses_title = models.CharField(max_length=30)
    uses_des = models.CharField(max_length=70)
