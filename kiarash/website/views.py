from django.shortcuts import render, redirect, get_object_or_404
from .models import AboutMe, Skills, Experience, MyWorks, ContactMe, HomePage, Recommendation, Greetings, SkillLevel
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import time
import json


def home_page(request):
      home = HomePage.objects.first()
      greetings = Greetings.objects.all().order_by("display_order").values()
      greeting_list = [g['greeting'] for g in greetings]
      print(greeting_list)
      about = AboutMe.objects.first()
      context = {'home':home, 'about': about, 'greetings':json.dumps(greeting_list)}
      return render(request, 'website/home.html', context)


def about_me(request):
    about = AboutMe.objects.first()
    my_recommendations = Recommendation.objects.all()
    context = {'about': about, 'my_recommendations': my_recommendations }
    return render(request, 'website/about.html', context)


def recommendation(request, id):
      recommendation_detail = get_object_or_404(Recommendation, pk=id)
      context = {"details" : recommendation_detail}
      return render(request, 'website/recommendation.html', context)
      


def skills(request):
	my_skills = Skills.objects.all()  
	skill_levels = SkillLevel.objects.all().order_by('display_order').values()

	skill_list = []
	for level in skill_levels:
		skill_list.append({'level':level.get('name'), 'skills': [s.name for s in my_skills if s.level.name == level.get('name')]})

	print(skill_list)
	my_exp = Experience.objects.all().order_by('-start_from').values()  
	context = {'my_skills': skill_list, 'my_exp': my_exp}
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
			contact_me = ContactMe(
				name=form.cleaned_data['name'],
				subject=form.cleaned_data['subject'],
				email_address=form.cleaned_data['email_address'],
				message=form.cleaned_data['message']
			)
			contact_me.save()

			# try:
			# 	send_mail(subject, message, 'kiarash.gh@gmail.com', ['kiarash.gh@gmail.com']) 
			# except BadHeaderError:
			# 	return HttpResponse('Invalid header found.')
			time.sleep(2)
			return redirect("/success")
		      
	form = ContactForm()
	return render(request, 'website/contact.html', {'form':form})


def success(request):
      return render(request, 'website/success.html', {})




      
      