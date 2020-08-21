from django.shortcuts import render
from .models import Project
from .models import Skills

# Create your views here.

def home(request):
    projects = Project.objects.all()
    content = {
        'projects' : projects
    }
    return render(request,'portfolio/home.html', content)

def about_me(request):
    return render(request,'portfolio/aboutme.html')

def skills(request):
    my_skill = Skills.objects.all()
    content = {
        'my_skill' : my_skill,
    }
    return render(request,'portfolio/skills.html', content)

