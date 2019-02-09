from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .models import LongURL
import random
import string

def generate_code():
    code = '' 
    for _ in range(8):
        # appends random letters and numbers to code variable
        code += random.choice(string.ascii_letters + string.digits)
    return code 
print(generate_code())

def index(request):
    if request.method == 'POST':
        
        #intsance of LongUrl class
        url = LongURL()
        #getting data from request
        url.url = request.POST['inputURL']
        url.code = generate_code()
        url.save()
        # render original page with the url instance
        return render(request, 'index.html', {'url': url})
    
        print(request.POST)

    return render(request, 'index.html')

'''
a function that directs generate_code to the url that was from the input fuction

'''
def redirect(request):
    location = request.GET.get('inputURL',)
    
    


 
