from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import guests_registration
# Register your models here
admin.site.register(guests_registration)