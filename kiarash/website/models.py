from django.db import models
from phonenumber_field.modelfields import PhoneNumberField 

# Create your models here.
# home


# About me
class AboutMe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title


#skill levels
class SkillLevel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

#skills
class Skills(models.Model):
    name = models.CharField(max_length=255)
    level = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

# my works
class MyWorks(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    #add pic

    def __str__(self) -> str:
        return self.title
    

# resume
class Resume(models.Model):
    job_title = models.CharField(max_length=255)
    start_from = models.DateField()
    end_to = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.job_title} - {self.start_from}"


# contact info
class ContactInfo(models.Model):
    title = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    mail = models.EmailField()

    def __str__(self) -> str:
        return self.title


# social media
class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    display_order = models.SmallIntegerField(default=0)
    # icon

    def __str__(self) -> str:
        return self.name



# contact me
class ContactMe(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email_address = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
