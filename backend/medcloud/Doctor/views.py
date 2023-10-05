
from django.http import JsonResponse

# Create your views here.



# add doctor function
def addDoctor(request):

    return JsonResponse({'text': 'Some JSON data is rendering'})


# get doctors
def getDoctors(request):

    return JsonResponse({'data': {"doctors":[{"name":'dr asad abudullah'}]}})

# get doctor by id
def getDoctorById(request):

    return JsonResponse({'data': {"doctors":[{"name":'dr asad abudullah'}]}})


# update doctor
def updateDoctor(request):

    return JsonResponse({'data': {"doctors":[{"name":'dr asad abudullah'}]}})

# search doctor
def searchDoctors(request):

    return JsonResponse({'data': {"doctors":[{"name":'dr asad abudullah'}]}})