from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Project, Experience, Education, Contact

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Contact)