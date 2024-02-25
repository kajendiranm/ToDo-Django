from django.urls import path
from . import views

urlpatterns = [
    path('post_feedback', views.feedback)
]
