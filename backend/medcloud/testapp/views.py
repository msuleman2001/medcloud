from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    msg = "test app"
    msg += "zain"
    return HttpResponse(msg)
