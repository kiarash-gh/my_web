from django.shortcuts import render
from .models import AboutMe, Skills, Experience, MyWorks

# Create your views here.

def about_me(request):
    about = AboutMe.objects.all()
    context = {'about': about[0]}
    return render(request, 'website/home.html', context)


def skills(request):
    my_skills = Skills.objects.all()  
    my_exp = Experience.objects.all().order_by('-start_from').values()  
    context = {'my_skills': my_skills, 'my_exp': my_exp}
    return render(request, 'website/skills.html', context)

def my_works(request):
    works = MyWorks.objects.all()
    context = {'works': works}
    return render(request, 'website/works.html', context)