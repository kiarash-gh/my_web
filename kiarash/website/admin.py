from django.contrib import admin
from .models import (
    AboutMe, 
    ContactInfo, 
    ContactMe, 
    Experience, 
    Greetings,
    HomePage, 
    MyWorks, 
    Recommendation,
    SkillLevel, 
    Skills, 
    SocialMedia, 
    )

# Register your models here.
admin.site.register(AboutMe)
admin.site.register(ContactInfo)
admin.site.register(Experience)
admin.site.register(HomePage)
admin.site.register(MyWorks)
admin.site.register(Recommendation)
admin.site.register(SocialMedia)


@admin.register(ContactMe)
class ModelDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address', 'subject', 'created_on')


@admin.register(Greetings)
class ModelDataAdmin(admin.ModelAdmin):
    list_display = ('greeting', 'display_order')

@admin.register(Skills)
class ModelDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

@admin.register(SkillLevel)
class ModelDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order')