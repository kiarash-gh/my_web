from django.shortcuts import render
from .models import AboutMe

# Create your views here.

def about_me(request):
    about = AboutMe.objects.all()
    context = {'about': about[0]}
    return render(request, 'website/home.html', context)