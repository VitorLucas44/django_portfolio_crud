from django.shortcuts import render, redirect
from .models import Skill
from .form import SkillForm

def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'portdjango/backoffice/skill_list.html', {'skills': skills})

def skill_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        percent = int(request.POST['percent'])
        skill = Skill(name=name, percent=percent)
        skill.save()
        return redirect('skill_list')
    return render(request, 'portdjango/backoffice/skill_create.html')

def skill_update(request, id):
    skill = Skill.objects.get(id=id)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
        
    else:
        form = SkillForm(instance=skill)
    return render(request, 'portdjango/backoffice/skill_edit.html', {'skill': skill})

def skill_delete(request, id):
    skill = Skill(id)
    skill.delete()
    return redirect('home')
