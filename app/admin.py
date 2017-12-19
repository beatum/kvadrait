from django.contrib import admin
from django.contrib.auth.admin import Group
from django.contrib.auth.models import User

from .models import Note

admin.site.register(Note)

admin.site.unregister(User)
admin.site.unregister(Group)

