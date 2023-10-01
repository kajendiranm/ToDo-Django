from django.contrib import admin
from .models import ProfileModel, TaskModel
# Register your models here.

admin.site.register(ProfileModel)
admin.site.register(TaskModel)