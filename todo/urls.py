from django.urls import path
from .views import login_page, register_page,home_page, logout_page, edit_page, add_page, delete_page, feedback_page
urlpatterns = [
    path('',home_page,name='home'),
    path('login',login_page,name='login'),
    path('logout',logout_page,name='logout'),
    path('register',register_page,name='register'),
    path('add',add_page,name='add'),
    path('edit/<int:id>',edit_page,name='edit'),
    path('delete/<int:id>',delete_page,name='delete'),
    path('feedback',feedback_page,name='feedback'),
]
