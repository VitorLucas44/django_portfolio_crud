from django.shortcuts import render, redirect
from .models import Services
from .forms import ServiceForms
# Create your views here.
def services(request) : 
    services = Services.objects.all()
    return render(request, 'portdjango/backoffice/services.html', {'services': services})
def destroy(request, id):
    destroy = Services(id)
    destroy.delete()
    return redirect('services')
def create(request):
    if request.method == 'POST':
        form = ServiceForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ServiceForms()
    return render(request, 'portdjango/backoffice/services_create.html', {'form': form})
def Serviceupdate(request, id):
    edit = Services.objects.get(id=id)
    if request.method == 'POST':
        form = ServiceForms(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ServiceForms(instance=edit)
    return render(request, 'portdjango/backoffice/service_edit.html', {'form': form})