from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
import pyshorteners

@csrf_protect
def shorten(request):   
    result=""
    if request.method == 'POST':
        origurl= request.POST["origurl"]  
        URL = origurl
        short_URL = pyshorteners.Shortener()
        result = short_URL.tinyurl.short(URL) 
        return JsonResponse({'result':result})
    else:
        return render(request,"shortener/index.html")
    