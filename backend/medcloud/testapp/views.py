from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    msg = "Suleman"
    msg += " Asad"
    msg += "Suleman updated"
    msg += "Asad updated"
    msg += "again suleman"
    msg += "asad here"
    msg += "suleman here"
    msg+="python dheeli hy"
    return HttpResponse(msg)