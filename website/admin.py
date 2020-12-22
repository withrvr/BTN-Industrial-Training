from django.contrib import admin
from .models import AboutModels, ExperienceModels, SkillModels, EducationModels, ContactModels

admin.site.register(AboutModels)
admin.site.register(ExperienceModels)
admin.site.register(SkillModels)
admin.site.register(EducationModels)
admin.site.register(ContactModels)


