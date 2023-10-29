from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class TaskModel(models.Model):
    user = models.ForeignKey(ProfileModel, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50,null=False)
    description = models.TextField(max_length=1000)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FeedbackModel(models.Model):
    user = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    comment = models.TextField()

    def __str__(self):
        return self.name
