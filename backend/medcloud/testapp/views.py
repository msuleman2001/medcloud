from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    msg = "test app"
<<<<<<< HEAD
    msg += "zain"
=======
    msg += "for zain"
>>>>>>> 574679860efad356a8616f1ad3d3ab186d5cca1a
    return HttpResponse(msg)
