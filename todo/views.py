from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ProfileModel, TaskModel, FeedbackModel
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_users, task_access
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def feedback_page(request):
    if request.method == "POST":
        name = request.POST['name']
        comment = request.POST['comment']
        name_required = False
        comment_required = False
        if name == '':
            name_required = True
        if comment == '':
            comment_required = True
        if name_required or comment_required == True:
            return render(request,'todo/feedback.html',{'name_required':name_required, 'comment_required':comment_required,'name':name,'comment':comment })
        else:
            FeedbackModel.objects.create(user=request.user.profilemodel, name=name,comment=comment)
            messages.success(request,'Thanks For Your Valuable Feedback!')
            return redirect('home')
    return render(request,'todo/feedback.html')
    

@login_required(login_url='login')
def home_page(request):
    tasks = request.user.profilemodel.taskmodel_set.all().order_by('complete','-created_at')#.order_by('-created_at')
    return render(request, 'todo/home.html',{'tasks':tasks})

@login_required(login_url='login')
def add_page(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        check = request.POST.get('check')
        if check is not None:
            check = True
        else:
            check = False
        if title == "":
            return render(request, 'todo/add.html',{'required':True,'description':description,})
        TaskModel.objects.create(user=request.user.profilemodel,title=title,description=description,complete=check)
        messages.success(request, "Task Added Successfully!")
        return redirect('home')
    return render(request, 'todo/add.html')

@login_required(login_url='login')
@task_access
def edit_page(request,id):
    if request.method == "POST":
        check = request.POST.get('check')
        task = TaskModel.objects.get(id=id)
        task.title = request.POST['title']
        task.description = request.POST['description']
        if check is not None:
            task.complete = True
        else:
            task.complete = False
        if task.title == "":
            return render(request, 'todo/edit.html',{'required':True})
        task.save()
        messages.success(request, "Task Edited Successfully!")
        return redirect('home')
    task = TaskModel.objects.get(id=id)
    return render(request,'todo/edit.html',{'task':task})

@login_required(login_url='login')
@task_access
def delete_page(request,id):
    if request.method == "POST":
        TaskModel.objects.get(id=id).delete()
        messages.success(request, "Task Deleted Successfully!")
        return redirect('home')
    return render(request,'todo/delete.html')



@unauthenticated_users
def login_page(request):
    if request.method == "POST":
        rec_form = LoginForm(request.POST)
        if rec_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are Logged In Successfully!")
                return redirect('home')
            else:
                return render(request, 'todo/login.html',{'form':rec_form,"error":True})
    form = LoginForm()
    return render(request, 'todo/login.html',{'form':form})

def logout_page(request):
    logout(request)
    messages.success(request, "You are Logged Out Successfully!")
    return redirect('login')

@unauthenticated_users
def register_page(request):
    if request.method == "POST":
        received_form = RegisterForm(request.POST)
        if received_form.is_valid():
            received_form.save()
            ProfileModel.objects.create(user=User.objects.get(username=request.POST['username']))
            messages.success(request, "Your account was created Successfully!")
            return redirect('login')
        else:
            return render(request, 'todo/register.html',{'form':received_form})
    form = RegisterForm()
    return render(request, 'todo/register.html',{'form':form})
