from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_me, name='about'),
    path('skills_and_experiences/', views.skills, name='skills'),
    path('skills_and_experiences/resume/<str:filename>', views.download_resume, name='download_resume'),
    path('my_works/', views.my_works, name='works'),
    path('contact_me/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('<str:id>/recommendation/', views.recommendation, name='rec'),
]


if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)