from django .shortcuts import redirect
from django.http import HttpResponse,Http404
from .models import TaskModel

def unauthenticated_users(view_func):
    def wrapperfunc(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapperfunc

def task_access(view_func):
    def wrapperfunc(request, *args, **kwargs):
        id = kwargs.get('id')
        task = TaskModel.objects.filter(user=request.user.profilemodel,id=id)
        if task:
            return view_func(request, *args, **kwargs)
        else:
            raise(Http404)
    return wrapperfunc