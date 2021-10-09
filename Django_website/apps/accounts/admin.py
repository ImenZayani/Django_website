from django.contrib import admin
from .models import UserInterest, UserPersona , UserProfile , UserInterest
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserPersona)
admin.site.register(UserInterest)