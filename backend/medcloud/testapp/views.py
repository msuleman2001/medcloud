from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    msg = "Suleman"
    msg += " Asad"
    msg += "Suleman updated"
    return HttpResponse(msg)