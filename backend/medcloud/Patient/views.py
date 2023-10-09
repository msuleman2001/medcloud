from django.http import JsonResponse
import json
from .models import Patient
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Create a new patient in the database


@csrf_exempt
def addPatient(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)

            # Create a new Patient object with the parsed data
            patient = Patient(
                patient_name=data['patient_name'],
                patient_phone_number=data['patient_phone_number'],
                patient_address=data['patient_address'],
                patient_gender=data['patient_gender'],
                patient_date_of_birth=data['patient_date_of_birth'],
                patient_guardian=data.get('patient_guardian', None),
                created_date_time=datetime.now(),
                created_by_id=data['created_by_id'],
                last_updated_date_time=datetime.now(),
                last_updated_id=data['last_updated_id'],
                is_enabled=data.get('is_enabled', True),
                remarks=data.get('remarks', None)
            )

            # Save the Patient object to the database
            patient.save()

            return JsonResponse({'message': 'Patient added successfully'})
        except KeyError:
            return JsonResponse({'error': 'Invalid JSON data format'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# Get a list of all patients


def getPatients(request):
    try:
        # Query all patients from the database
        patients = Patient.objects.all()

        # Serialize the queryset to JSON format
        serialized_patients = [
            {
                'patient_id': patient.patient_id,
                'patient_name': patient.patient_name,
                'patient_phone_number': patient.patient_phone_number,
                'patient_address': patient.patient_address,
                'patient_gender': patient.patient_gender,
                'patient_date_of_birth': patient.patient_date_of_birth,
                'patient_guardian': patient.patient_guardian,
                'created_date_time': patient.created_date_time,
                'created_by_id': patient.created_by_id,
                'last_updated_date_time': patient.last_updated_date_time,
                'last_updated_id': patient.last_updated_id,
                'is_enabled': patient.is_enabled,
                'remarks': patient.remarks,
            }
            for patient in patients
        ]

        # Create a JSON response with the serialized data
        response_data = {'patients': serialized_patients}

        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Get a list of patients according to filters (you can implement this as needed)


def searchPatients(request):
    try:
        # Get a dictionary of query parameters from the request
        query_params = request.GET.dict()
        # Implement your filtering logic based on query_params here

        # Example filtering:
        # patients = Patient.objects.filter(patient_name__icontains=query_params.get('name', ''))

        return JsonResponse({'message': 'Search functionality to be implemented'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
