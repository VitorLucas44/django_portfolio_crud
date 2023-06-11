from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=30)
    percent = models.IntegerField()
