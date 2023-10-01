from django.contrib import admin
from .models import ProfileModel, TaskModel, FeedbackModel
# Register your models here.

admin.site.register(ProfileModel)
admin.site.register(TaskModel)
admin.site.register(FeedbackModel)