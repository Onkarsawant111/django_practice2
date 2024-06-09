from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Uses(models.Model):
    uses_title = models.CharField(max_length=30)
    uses_des = models.CharField(max_length=500)
