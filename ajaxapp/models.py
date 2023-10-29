from django.db import models

# Create your models here.

class NameModel(models.Model):
    user_name = models.CharField(max_length=15,unique=True)

    def __str__(self):
        return self.user_name