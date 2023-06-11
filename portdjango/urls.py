"""
URL configuration for portdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front.views import *
from about.views import *
from skill.views import *
from contact.views import *
from services.views import *
from testimonial.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('backoffice/', get, name='backoffice'),
    path('backoffice/edit/about', edit_about, name='e_about'),
    path('skills/', skill_list, name='skill_list'),
    path('skills/create/', skill_create, name='skill_create'),
    path('skills/update/<int:id>/', skill_update, name='skill_update'),
    path('skills/delete/<int:id>/', skill_delete, name='skill_delete'),
    path('contact/', Contactupdate, name='contact'),
    path('services/', services, name='services'),
    path('services/create/', create, name='servicescreate'),
    path('services/<int:id>', Serviceupdate, name='serviceedit'),
    path('services/destroy/<int:id>', destroy),
    path('testimonial/', testimonials, name='testimonials'),
    path('testimonial/create/', create, name='testimonialscreate'),
    path('testimonials/<int:id>', testimonialsupdate, name='testimonialsedit'),
    path('testimonials/destroy/<int:id>', destroy),
]