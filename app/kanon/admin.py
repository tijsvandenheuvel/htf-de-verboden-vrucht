from django.contrib import admin

# Register your models here.
from .models import Kanon,Munition,User

admin.site.register(Kanon)
admin.site.register(Munition)
admin.site.register(User)