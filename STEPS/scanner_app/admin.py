from django.contrib import admin
from .models import Scanner,Event,User

admin.site.register(Scanner)
admin.site.register(Event)
admin.site.register(User)