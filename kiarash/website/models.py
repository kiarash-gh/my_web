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
    
    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"


#skill levels
class SkillLevel(models.Model):
    name = models.CharField(max_length=255)

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
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    #add pic

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
    # icon

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


