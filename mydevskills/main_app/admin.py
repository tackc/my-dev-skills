from django.contrib import admin
from .models import User, Skill, Note

# Register your models here.
admin.site.register(User)
admin.site.register(Skill)
admin.site.register(Note)