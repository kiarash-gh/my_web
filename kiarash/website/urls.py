from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.about_me, name='about'),
    path('skills_and_experiences/', views.skills, name='skills'),
    path('my_works/', views.my_works, name='works'),
    path('contact_me/', views.contact, name='contact'),
]
