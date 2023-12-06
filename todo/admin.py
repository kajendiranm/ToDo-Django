from django.contrib import admin
from .models import ProfileModel, TaskModel, FeedbackModel
# Register your models here.

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['title','user']

admin.site.register(ProfileModel)
admin.site.register(TaskModel,TaskModelAdmin)
admin.site.register(FeedbackModel)