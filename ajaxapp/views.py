from django.shortcuts import render
from .models import NameModel
from django.http import JsonResponse
# Create your views here.


def home(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        name = request.POST.get('name')
        obj = NameModel.objects.filter(user_name=name)
        if obj.exists():
            avail = False
        else:
            avail = True
        return JsonResponse({'avail':avail,'name':name})
    return render(request, 'index.html')

def add(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        name = request.POST.get('name')
        NameModel.objects.create(user_name=name)
        return JsonResponse({'name':name})