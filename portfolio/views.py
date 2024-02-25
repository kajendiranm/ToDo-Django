from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback
# Create your views here.

@csrf_exempt
def feedback(request):
    if request.method == 'POST':
        referer = request.META.get('HTTP_REFERER', None)
        if referer:
            from urllib.parse import urlparse
            if urlparse(referer).netloc == '127.0.0.1:5500':
                name = request.POST.get('name')
                email = request.POST.get('email')
                message = request.POST.get('message')
                Feedback.objects.create(name = name, email = email, message = message)
                return JsonResponse({'name':name})
    else:
        return HttpResponse('Nothing to show')
    