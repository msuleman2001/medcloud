
from django.http import JsonResponse

# Create your views here.


# add a new Patient in database


def addPatient(request):
    return JsonResponse({'text': 'Some JSON data is rendering'})

# get list of all Patient


def getPatient(request):
    return JsonResponse({'data': {"Patients": [{"name": 'moosa'}]}})

# get a single Patient record


def getPatientById(request):
    return JsonResponse({'data': {"Patients": [{"name": 'moosa'}]}})


# update an existing Patient
def updatePatient(request):
    return JsonResponse({'data': {"Patients": [{"name": 'moosa'}]}})

# get list of Patients according to filter


def searchPatient(request):
    return JsonResponse({'data': {"Patients": [{"name": 'moosa'}]}})
