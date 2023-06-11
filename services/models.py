from django.db import models

# Create your models here.
class Services(models.Model):
    ICON_CHOICES = (
        ('bi-briefcase', 'Briefcase'),
        ('bi-card-checklist', 'Card Checklist'),
        ('bi-bar-chart', 'Bar Chart'),
        ('bi-binoculars', 'Binoculars'),
        ('bi-brightness-high', 'High Brightness'),
        ('bi-calendar4-week', 'Calendar (4 weeks)'),
    )
    title_services = models.CharField(max_length=50)
    descriptions = models.TextField(max_length=200)
    icon = models.CharField(max_length=30, choices=ICON_CHOICES)