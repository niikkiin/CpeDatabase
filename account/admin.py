from django.contrib import admin
from account.models import UserProfileInfo, Log
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(Log)