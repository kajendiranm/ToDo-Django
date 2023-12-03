from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("add",views.add)
    #add /add while production if main url with "add" withour /
]
