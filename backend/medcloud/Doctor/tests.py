# from django.test import TestCase
# from django.urls import reverse
# from django.http import JsonResponse
# from .models import Doctor
# import json
# from django.contrib.auth.models import User

# class DoctorViewTestCase(TestCase):
#     def test_add_doctor(self):
#         # Define the data for the new doctor to be added
#         new_doctor_data = {
#             'name': 'New Doctor',
#             'email': 'newdoctor@example.com',
#             'phone': '987-654-3210',
#             'license': '54321',  # Corrected key to 'license'
#             'speciality': 'Neurology',
#             'start_year': 2010,
#             'clinic_address': '789 Elm St',
#             'added_by_id': 3,
#             'remarks': 'Test remarks for New Doctor'
#         }

#         # Create a JSON string from the new doctor data
#         new_doctor_data_json = json.dumps(new_doctor_data)

#         # Test the addDoctor view by making a POST request
#         url = reverse('doctors')  # Assuming you have defined a URL pattern with the name 'doctors'
#         response = self.client.post(url, data=new_doctor_data_json, content_type='application/json')

#         # Check if the response status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)

#         # Check if the response contains the expected message
#         expected_response = {'message': 'Doctor added successfully'}
#         self.assertEqual(response.json(), expected_response)

#         # Verify that the new doctor has been added to the database
#         new_doctor = Doctor.objects.get(name='New Doctor')
#         self.assertIsNotNone(new_doctor)
#         # Add more assertions to verify the data of the new doctor if needed
    
#     def setUp(self):
#         # Create a user (assuming 'User' is the model for the added_by_id field)
#         user = User.objects.create(username="testuser")

#         # Create some sample doctors in the database for testing
#         Doctor.objects.create(
#             name="Dr. John Doe",
#             speciality="Cardiology",
#             start_year=2005,
#             added_by_id=user.id  # Provide the ID of the user as the added_by_id
#         )
#         Doctor.objects.create(
#             name="Dr. Jane Smith",
#             speciality="Dermatology",
#             start_year=2008,
#             added_by_id=user.id
#         )
#         Doctor.objects.create(
#             name="Dr. Michael Brown",
#             speciality="Orthopedics",
#             start_year=2010,
#             added_by_id=user.id
#         )
#         # Add more sample doctors as needed

#     def test_get_doctors_with_filter(self):
#         # Define the filter criteria
#         filters = {'name': 'John', 'speciality': 'Cardiology'}

#         # Generate the URL for your getDoctors view, including filter criteria
#         url = reverse('getDoctors')  # Replace 'get_doctors' with your actual URL name

#         # Make a GET request with the filter criteria
#         response = self.client.get(url, data=filters)

#         # Check if the response status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)

#         # Check if the filtered doctor's name is in the response content
#         self.assertContains(response, 'Dr. John Doe')

#         # You can add more assertions based on the expected results

#     def test_get_doctors_without_filter(self):
#         # Generate the URL for your getDoctors view without filter criteria
#         url = reverse('getDoctors')  # Replace 'get_doctors' with your actual URL name

#         # Make a GET request without filter criteria
#         response = self.client.get(url)

#         # Check if the response status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)

    
    
    

# # {
# #       "email": "abc10@gmail.com",
# #       "name": "Asad",
# #       "phone": "+923440059960",
# #       "license": "abc123",
# #       "speciality": "Ophthalmologist",
# #       "start_year": "2018",
# #       "clinic_address": "BWP",
# #       "country": "Pakistan",
# #       "added_by_id": "1",
# #       "remarks": "Nothing"
# #     },
# #     {
# #       "email": "abc11@gmail.com",
# #       "name": "Asad",
# #       "phone": "+923440059961",
# #       "license": "abc123",
# #       "speciality": "Ophthalmologist",
# #       "start_year": "2018",
# #       "clinic_address": "BWP",
# #       "country": "Pakistan",
# #       "added_by_id": "1",
# #       "remarks": "Nothing"
# #     },
# #     {
# #       "email": "abc12@gmail.com",
# #       "name": "Asad",
# #       "phone": "+923440059962",
# #       "license": "abc123",
# #       "speciality": "Ophthalmologist",
# #       "start_year": "2018",
# #       "clinic_address": "BWP",
# #       "country": "Pakistan",
# #       "added_by_id": "1",
# #       "remarks": "Nothing"
# #     },
# #     {
# #       "email": "abc13@gmail.com",
# #       "name": "Asad",
# #       "phone": "+923440059963",
# #       "license": "abc123",
# #       "speciality": "Ophthalmologist",
# #       "start_year": "2018",
# #       "clinic_address": "BWP",
# #       "country": "Pakistan",
# #       "added_by_id": "1",
# #       "remarks": "Nothing"
# #     },
# #     {
# #       "email": "abc14@gmail.com",
# #       "name": "Asad",
# #       "phone": "+923440059964",
# #       "license": "abc123",
# #       "speciality": "Ophthalmologist",
# #       "start_year": "2018",
# #       "clinic_address": "BWP",
# #       "country": "Pakistan",
# #       "added_by_id": "1",
# #       "remarks": "Nothing"
# #     }

from rest_framework.test import APIClient
from django.test import TestCase
from .models import Doctor

class DoctorTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.doctor_data = {
            'email': 'doctor@example.com',
            'name': 'John Doe',
            # Add other fields as needed
        }
        self.doctor = Doctor.objects.create(**self.doctor_data)

    def test_create_doctor(self):
        response = self.client.post('/doctors/', self.doctor_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_doctor(self):
        response = self.client.get(f'/doctors/detail/?query={self.doctor.id}')
        self.assertEqual(response.status_code, 200)

    def test_update_doctor(self):
        updated_data = {'name': 'Updated Name'}
        response = self.client.put(f'/doctors/detail/?query={self.doctor.id}', updated_data, format='json')
        self.assertEqual(response.status_code, 200)