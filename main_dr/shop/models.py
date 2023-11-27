from django.db import models

class Figure(models.Model):
    shape = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
   

# Create your models here.
