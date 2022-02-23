from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
import pyshorteners

@csrf_protect
def shorten(request):   
    result=""
    if request.method == 'POST':
        origurl= request.POST["origurl"] 
        print(origurl) 
        URL = origurl
        short_URL = pyshorteners.Shortener()
        result = short_URL.tinyurl.short(URL)
        print("Shortened URL: "+result)  
    else:
        print("Else block")
    return render(request,'shortener/index.html',{'result':result})