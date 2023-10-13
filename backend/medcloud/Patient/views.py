from django.http import JsonResponse
import json
from .models import Patient
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
# Create a new patient in the database


@csrf_exempt
def addPatient(request):
    if request.method == 'POST':

        try:
            # Parse the incoming JSON data as an array of objects
            data = json.loads(request.body)
            new_patient_id = 0
            # Ensure that data is a list
            if not isinstance(data, list):
                new_patient_id = savePatient(data)
            # Iterate over each object in the array and create a Patient object for each
            else:
                for item in data:
                    # Create a new Patient object with the parsed data
                    new_patient_id = savePatient(item)

            return JsonResponse({'message': 'Patients added successfully', 'new_patient_id': new_patient_id})
        except KeyError:
            return JsonResponse({'error': 'Invalid JSON data format in one or more objects'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def savePatient(patient_item):
    t = type(patient_item)
    patient = Patient(
        patient_name=patient_item['patient_name'],
        patient_phone_number=patient_item['patient_phone_number'],
        patient_address=patient_item['patient_address'],
        patient_gender=patient_item['patient_gender'],
        patient_date_of_birth=patient_item['patient_date_of_birth'],
        patient_guardian=patient_item.get('patient_guardian', None),
        created_date_time=datetime.now(),
        created_by_id=patient_item['created_by_id'],
        last_updated_date_time=datetime.now(),
        last_updated_id=patient_item['last_updated_id'],
        is_enabled=patient_item.get('is_enabled', True),
        remarks=patient_item.get('remarks', None)
    )

    # Save the Patient object to the database
    patient.save()
    return patient.patient_id
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


def getPatients(request):
    try:
        # Get parameters from the request
        # Default to page 1 if not specified
        page_number = int(request.GET.get('page', 1))
        # Default to 10 records per page
        records_per_page = int(request.GET.get('records_per_page', 10))

        # Query all patients from the database
        patients = Patient.objects.all()

        # Create a Paginator object
        paginator = Paginator(patients, records_per_page)

        # Get the specified page
        try:
            current_page = paginator.page(page_number)
        except EmptyPage:
            return JsonResponse({'error': 'Invalid page number'}, status=400)

        # Serialize the paginated data to JSON format
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
            for patient in current_page
        ]

        # Create a JSON response with the serialized data
        response_data = {
            'patients': serialized_patients,
            'page_number': current_page.number,
            'total_pages': paginator.num_pages,
            'total_records': paginator.count,
        }

        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


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


@csrf_exempt
def updatePatient(request, patient_id):
    if request.method == 'PUT':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)

            # Get the patient to update
            patient = Patient.objects.get(patient_id=patient_id)

            # Update the patient's information based on the parsed data
            patient.patient_name = data['patient_name']
            patient.patient_phone_number = data['patient_phone_number']
            patient.patient_address = data['patient_address']
            patient.patient_gender = data['patient_gender']
            patient.patient_date_of_birth = data['patient_date_of_birth']
            patient.patient_guardian = data.get('patient_guardian', None)
            patient.last_updated_date_time = datetime.now()
            patient.last_updated_id = data['last_updated_id']
            patient.is_enabled = data.get('is_enabled', True)
            patient.remarks = data.get('remarks', None)

            # Save the updated patient object to the database
            patient.save()

            return JsonResponse({'message': 'Patient updated successfully'})
        except (KeyError, Patient.DoesNotExist):
            return JsonResponse({'error': 'Invalid JSON data format or patient not found'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
