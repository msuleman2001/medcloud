# from django.http import JsonResponse
# import json
# from .models import Doctor
# from django.views.decorators.csrf import csrf_exempt
# from datetime import datetime
# from django.core import serializers
# from django.core.exceptions import ObjectDoesNotExist
# from django.core.paginator import Paginator
# # Create your views here.
# # add a new doctor in database
# @csrf_exempt
# def addDoctor(request):
#     if request.method == 'POST':
#         try:
#             # Parse the incoming JSON data
#             data = json.loads(request.body)
            
#             # Create a new Doctor object with the parsed data
#             doctor = Doctor(
#                 email=data['email'],
#                 name=data['name'],
#                 phone=data['phone'],
#                 license_no=data['license'],  # Corrected key to 'license'
#                 speciality=data['speciality'],
#                 start_year=data['start_year'],
#                 clinic_address=data['clinic_address'],
#                 country='pakistan',  # Corrected key to 'country'
#                 added_by_id=data['added_by_id'],
#                 added_datetime=datetime.now(),
#                 last_update_date_time=datetime.now(),
#                 remarks=data['remarks'],
#                 is_enabled=False,
                
#             )
            
#             # Save the Doctor object to the database
#             doctor.save()
            
#             return JsonResponse({'message': 'Doctor added successfully'})
#         except KeyError:
#             return JsonResponse({'error': 'Invalid JSON data format'}, status=400)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)




# # get list of all doctors
# @csrf_exempt
# def getDoctors(request):
#     try:
#         # Get query parameters for pagination
#         page_number = request.GET.get('page', 1)
#         per_page = request.GET.get('per_page', 10)

#         # Build a dictionary to hold filter criteria
#         filters = {}
#         for param, value in request.GET.items():
#             if param in ['page', 'per_page']:
#                 continue  # Skip pagination parameters
#             filters[f'{param}__icontains'] = value  # Assume case-insensitive substring matching

#         # Query doctors from the database with the dynamic filters
#         doctors = Doctor.objects.filter(**filters)

#         # Create a paginator with the filtered queryset
#         paginator = Paginator(doctors, per_page)

#         # Get the specified page
#         page = paginator.page(page_number)

#         # Serialize the queryset to JSON format
#         serialized_doctors = [
#             {
#                 'id': doctor.id,
#                 'name': doctor.name,
#                 # Add other fields as needed
#             }
#             for doctor in page
#         ]

#         # Create a JSON response with the serialized data
#         response_data = {
#             'doctors': serialized_doctors,
#             'total_pages': paginator.num_pages,
#             'current_page': page_number,
#             'total_records': paginator.count,
#             'records_per_page': per_page,
#         }

#         return JsonResponse(response_data)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# # get list of doctors according to filter

# @csrf_exempt    
# def updateDoctor(request):
#     try:
#         # Get the 'query' parameter from the request
#         query = request.GET.get('query')

#         # Parse the JSON data from the request body
#         data = json.loads(request.body)

#         # Query the doctor based on the 'query' parameter
#         doctor = Doctor.objects.get(pk=query)

#         # Update the doctor's information with the provided data
#         for field, value in data.items():
#             setattr(doctor, field, value)

#         # Save the updated doctor object to the database
#         doctor.save()

#         return JsonResponse({'message': 'Doctor updated successfully'})
#     except Doctor.DoesNotExist:
#         return JsonResponse({'error': 'Doctor not found'}, status=404)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)
from .models import Doctor
from .serializer import DoctorSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class addDoctor(APIView):
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Doctor added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getDoctors(APIView):
    def get(self, request):
        query = request.query_params.get('query')
        try:
            doctor = Doctor.objects.get(pk=query)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

    # def updateDoctor(self, request):
    #     query = request.query_params.get('query')
    #     try:
    #         doctor = Doctor.objects.get(pk=query)
    #         serializer = DoctorSerializer(doctor, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response({'message': 'Doctor updated successfully'})
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Doctor.DoesNotExist:
    #         return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)


class updateDoctor(APIView):
    def put(self, request):
        query = request.query_params.get('query')
        try:
            doctor = Doctor.objects.get(pk=query)
            serializer = DoctorSerializer(doctor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Doctor updated successfully'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)