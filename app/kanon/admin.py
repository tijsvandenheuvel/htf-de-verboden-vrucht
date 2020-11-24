from django.contrib import admin

# Register your models here.
from .models import Kanon,User

admin.site.register(Kanon)

admin.site.register(User)