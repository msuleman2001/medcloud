from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    msg = "Hi i am doctor"
    
    return HttpResponse(msg)