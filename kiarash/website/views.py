from django.shortcuts import render, redirect
from .models import AboutMe, Skills, Experience, MyWorks
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

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

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Contact Form" 
			body = {
			'first_name': form.cleaned_data['name'], 
			'last_name': form.cleaned_data['subject'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'kiarash.gh@gmail.com', ['kiarash.gh@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:homepage")
      
	form = ContactForm()
	return render(request, "website/contact.html", {'form':form})