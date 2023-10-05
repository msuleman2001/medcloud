
from django.http import JsonResponse

# Create your views here.
# add a new doctor in database
def addDoctor(request):
    return JsonResponse({'text': 'Some JSON data is rendering'})

# get list of all doctors
def getDoctors(request):
    return JsonResponse({'data': {"doctors":[{"name":'dr asad abudullah'}]}})
    
# get a single doctor record
def getDoctorById(request):
    return JsonResponse({'data': {"doctors":[{"name":'dr asad abudullah'}]}})


# update an existing doctor
def updateDoctor(request):
    return JsonResponse({'data': {"doctors":[{"name":'dr asad abudullah'}]}})

# get list of doctors according to filter
def searchDoctors(request):
    return JsonResponse({'data': {"doctors":[{"name":'dr asad abudullah'}]}})
