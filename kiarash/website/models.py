from django.db import models
from phonenumber_field.modelfields import PhoneNumberField 
from uuid import uuid4
import os

def custom_upload_name(instance, filename):    
    upload_to = instance.upload_to
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid4().hex}"
    filename = f"{instance.file_name}_{unique_filename}.{ext}"
    return os.path.join(upload_to, filename)


# home
class HomePage(models.Model):
    profile_image = models.ImageField(upload_to='profile')
    greetings = models.TextField(blank=True, null=True)

class Greetings(models.Model):
    greeting = models.CharField(max_length=255)
    display_order = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.greeting
    
    class Meta:
        verbose_name = "Greeting"
        verbose_name_plural = "Greetings"
    


# About me
class AboutMe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"


#skill levels
class SkillLevel(models.Model):
    name = models.CharField(max_length=255)
    display_order = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Skill Level"
        verbose_name_plural = "Skill Levels"

#skills
class Skills(models.Model):
    name = models.CharField(max_length=255)
    level = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

# my works
class MyWorks(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='my_work', null=True)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)  

    def __str__(self) -> str:
        return self.title
        
    class Meta:
        verbose_name = "My Work"
        verbose_name_plural = "My Works"

# resume
class Experience(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_website = models.URLField(null=True, blank=True)
    start_from = models.DateField()
    end_to = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.job_title} - {self.start_from}"
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"


# resume file
class Resume(models.Model):
    file_name = models.CharField(max_length=255)
    resume = models.FileField(upload_to=custom_upload_name, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.file_name
    
    @property
    def upload_to(self):
        return os.path.join('resume')
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.resume.name = custom_upload_name(self, self.resume.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resume"

# contact info
class ContactInfo(models.Model):
    title = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    mail = models.EmailField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"


# social media
class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    display_order = models.SmallIntegerField(default=0)
    icon = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Medias"


# contact me
class ContactMe(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email_address = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Contanct Me"
        verbose_name_plural = "Contact Me"


#recommendations
class Recommendation(models.Model):
    recommender = models.CharField(max_length=255)
    recommender_profile_image = models.ImageField(upload_to='recommender')
    recommender_profile_url = models.URLField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.recommender
    

class Hobbies(models.Model):
    hobbie = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.hobbie
    
    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'