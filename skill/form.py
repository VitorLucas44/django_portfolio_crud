from django import forms
from .models import Skill

class SkillForm(forms.ModelForm):
    percent = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'min': '0', 'max': '100'}))
    class Meta:
        model = Skill
        fields = '__all__'
