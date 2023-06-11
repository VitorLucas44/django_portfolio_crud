from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    description = models.TextField(max_length=200)