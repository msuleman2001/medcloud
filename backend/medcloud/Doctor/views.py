from django.http import JsonResponse
import json
from .models import Doctor
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
# add a new doctor in database
@csrf_exempt
def addDoctor(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
            
            # Create a new Doctor object with the parsed data
            doctor = Doctor(
                email=data['email'],
                name=data['name'],
                phone=data['phone'],
                license_no=data['license'],  # Corrected key to 'license'
                speciality=data['speciality'],
                start_year=data['start_year'],
                clinic_address=data['clinic_address'],
                country='pakistan',  # Corrected key to 'country'
                added_by_id=data['added_by_id'],
                added_datetime=datetime.now(),
                last_update_date_time=datetime.now(),
                is_enabled=False,
                remarks=data['remarks']
            )
            
            # Save the Doctor object to the database
            doctor.save()
            
            return JsonResponse({'message': 'Doctor added successfully'})
        except KeyError:
            return JsonResponse({'error': 'Invalid JSON data format'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




# get list of all doctors
def getDoctors(request):
    try:
        # Query all doctors from the database
        doctors = Doctor.objects.all()

        # Serialize the queryset to JSON format, excluding the 'id' field
        serialized_doctors = [
            {
                'id' : doctor.id,
               'name': doctor.name,
               'email': doctor.email,
               'phone': doctor.phone,
               "license_no" : doctor.license_no,
               "start_year" : doctor.start_year,
               "clinic_address" : doctor.clinic_address,
               "country" : doctor.country,
               "added_by_id" : doctor.added_by_id,
               "added_datetime" : doctor.added_datetime,
               "last_update_date_time" : doctor.last_update_date_time,
               "is_enabled" : doctor.is_enabled,
               'speciality': doctor.speciality,
                # Add more fields as needed
            }
            for doctor in doctors
        ]

        # Create a JSON response with the serialized data
        response_data = {'doctors': serialized_doctors}

        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# get list of doctors according to filter
def searchDoctors(request):
    try:
        # Get a dictionary of query parameters from the request
        query_params = request.GET.dict()

        # Create a queryset that initially includes all doctors
        doctors = Doctor.objects.all()

        # Apply filters based on query parameters
        for field, value in query_params.items():
            # Use case-insensitive partial match for all fields
            filter_arg = f"{field}__icontains"
            doctors = doctors.filter(**{filter_arg: value})

        # Serialize the queryset to JSON format
        serialized_doctors = [
            {
                'id' : doctor.id,
               'name': doctor.name,
               'email': doctor.email,
               'phone': doctor.phone,
               "license_no" : doctor.license_no,
               "start_year" : doctor.start_year,
               "clinic_address" : doctor.clinic_address,
               "country" : doctor.country,
               "added_by_id" : doctor.added_by_id,
               "added_datetime" : doctor.added_datetime,
               "last_update_date_time" : doctor.last_update_date_time,
               "is_enabled" : doctor.is_enabled,
               'speciality': doctor.speciality,
                 # Add more fields as needed
            }
            for doctor in doctors
        ]
        # Create a JSON response with the serialized data
        response_data = {'doctors': serialized_doctors}

        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt    
def updateDoctor(request):
    try:
        # Get the 'query' parameter from the request
        query = request.GET.get('query')

        # Parse the JSON data from the request body
        data = json.loads(request.body)

        # Query the doctor based on the 'query' parameter
        doctor = Doctor.objects.get(pk=query)

        # Update the doctor's information with the provided data
        for field, value in data.items():
            setattr(doctor, field, value)

        # Save the updated doctor object to the database
        doctor.save()

        return JsonResponse({'message': 'Doctor updated successfully'})
    except Doctor.DoesNotExist:
        return JsonResponse({'error': 'Doctor not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)