from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(UserContact)
admin.site.register(Framework)
admin.site.register(MyProfil)

class AdminMessage(admin.ModelAdmin):
    list_display = ("name",  "email", "phone_number", "message")