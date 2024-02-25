from django.contrib import admin
from .models import Feedback

# Register your models here.


class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at',)  # Add other fields if needed

admin.site.register(Feedback, FeedbackModelAdmin)