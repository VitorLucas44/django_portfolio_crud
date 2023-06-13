from django.shortcuts import render
from about.models import About
from skill.models import Skill
from services.models import Services
from contact.models import Contact
from testimonial.models import Testimonial

def home(request):
    return render(request, 'portdjango/front/index.html', {'about': About.objects.all()[0], 'skills': Skill.objects.all(), 'services': Services.objects.all(), 'contact': Contact.objects.all()[0], 'testimonials': Testimonial.objects.all()})