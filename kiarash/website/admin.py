from django.contrib import admin
from .models import AboutMe, ContactInfo, SkillLevel, Skills, SocialMedia, MyWorks, Experience, ContactMe, HomePage

# Register your models here.
admin.site.register(HomePage)
admin.site.register(AboutMe)
admin.site.register(ContactInfo)
admin.site.register(SkillLevel)
admin.site.register(SocialMedia)
admin.site.register(MyWorks)
admin.site.register(Experience)


@admin.register(Skills)
class ModelDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

@admin.register(ContactMe)
class ModelDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address', 'subject', 'created_on')