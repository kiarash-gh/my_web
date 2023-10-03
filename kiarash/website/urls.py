from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.about_me, name='about')
]
