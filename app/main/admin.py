from django.contrib import admin

# Register your models here.
from .models import User,Mood

admin.site.register(User)
admin.site.register(Mood)