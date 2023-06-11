from django.shortcuts import render, redirect
from django.views import View
from .models import About
from .form import AboutForm

def get(request):
    about = About.objects.all()
    return render(request, 'portdjango/backoffice/backoffice.html', {'about': about})


def post(request):
    about = About.objects.all().first()
    about.description = request.POST.get('description')
    about.birthday = request.POST.get('birthday')
    about.website = request.POST.get('website')
    about.phone = request.POST.get('phone')
    about.city = request.POST.get('city')
    about.age = request.POST.get('age')
    about.degree = request.POST.get('degree')
    about.email = request.POST.get('email')
    about.freelance = request.POST.get('freelance')
    about.save()
    return redirect('portdjango/front/index.html')

def edit_about(request):
    edit = About.objects.all()[0]
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AboutForm(instance=edit)
    return render(request, 'portdjango/backoffice/editabout.html', {'form': form})
