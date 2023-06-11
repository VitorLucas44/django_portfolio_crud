from django import forms
from .models import Testimonial

class TestimonialsForms(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'