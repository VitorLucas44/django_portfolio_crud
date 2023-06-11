from django.db import models

class About(models.Model):
    description = models.TextField()
    birthday = models.DateField()
    website = models.URLField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance = models.BooleanField(default=False)
