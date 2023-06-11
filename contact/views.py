from django.shortcuts import render, redirect
from .models import Contact
from .form import ContactForms
# Create your views here.

def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'portdjango/backoffice/contact.html', {'contacts': contacts})


def Contactupdate(request):
    edit = Contact.objects.get(id=1)
    if request.method == 'POST':
        form = ContactForms(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForms(instance=edit)
    return render(request, 'portdjango/backoffice/contact.html', {'form': form})