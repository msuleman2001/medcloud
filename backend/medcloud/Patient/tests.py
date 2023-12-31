# from django.test import TestCase, Client
# from django.urls import reverse
# from .models import Patient
# import json
# from datetime import datetime


# class PatientViewsTest(TestCase):

#     def test_addPatient(self):
#         url = reverse('add_patient')
#         data = [
#             {
#                 "patient_name": "John Doe",
#                 "patient_phone_number": "123-456-7890",
#                 "patient_address": "123 Main St, City",
#                 "patient_gender": "Male",
#                 "patient_date_of_birth": "1990-01-15",
#                 "created_date_time": datetime.now().isoformat(),
#                 "created_by_id": 1,
#                 "last_updated_date_time": datetime.now().isoformat(),
#                 "last_updated_id": 1,
#                 "is_enabled": True,
#                 "remarks": "This is a sample patient."
#             },
#             {
#                 "patient_name": "Jane Smith",
#                 "patient_phone_number": "987-654-3210",
#                 "patient_address": "456 Elm St, Town",
#                 "patient_gender": "Female",
#                 "patient_date_of_birth": "1985-05-20",
#                 "created_date_time": datetime.now().isoformat(),
#                 "created_by_id": 2,
#                 "last_updated_date_time": datetime.now().isoformat(),
#                 "last_updated_id": 2,
#                 "is_enabled": False,
#                 "remarks": "Another sample patient."
#             }
#         ]

#         response = self.client.post(url, json.dumps(
#             data), content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(Patient.objects.count(), 22)

#     def test_getPatients(self):
#         url = reverse('get_patients')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         # You can add more assertions to check the content of the response

#     def setUp(self):
#         # Create sample patient data for testing
#         for i in range(20):
#             Patient.objects.create(
#                 patient_name=f"Patient {i}",
#                 patient_phone_number="123-456-7890",
#                 patient_address="123 Main St",
#                 patient_gender="Male",
#                 patient_date_of_birth="2000-01-01",
#                 created_date_time="2023-10-11 12:00:00",
#                 created_by_id=1,
#                 last_updated_date_time="2023-10-11 12:00:00",
#                 last_updated_id=1,
#                 is_enabled=True,
#                 remarks="Sample remarks",
#             )

#     def test_pagination(self):
#         # Replace 'get_patients' with your URL name
#         response = self.client.get(reverse('get_patients'))
#         self.assertEqual(response.status_code, 200)
#         data = response.json()

#         # Check the response structure and content
#         self.assertIn('patients', data)
#         self.assertIn('page_number', data)
#         self.assertIn('total_pages', data)
#         self.assertIn('total_records', data)
#         # Default records per page is 10
#         self.assertEqual(len(data['patients']), 10)
#         self.assertEqual(data['page_number'], 1)
#         self.assertEqual(data['total_pages'], 2)
#         self.assertEqual(data['total_records'], 20)

#     def test_pagination_with_custom_parameters(self):
#         # Your test code here

#         response = self.client.get(reverse('get_patients'), {
#             'page': 2, 'records_per_page': 5})
#         self.assertEqual(response.status_code, 200)
#         data = response.json()

#         # Check the response content with custom parameters
#         self.assertIn('patients', data)
#         self.assertIn('page_number', data)
#         self.assertIn('total_pages', data)
#         self.assertIn('total_records', data)
#         # Custom records per page is 5
#         self.assertEqual(len(data['patients']), 5)
#         self.assertEqual(data['page_number'], 2)
#         self.assertEqual(data['total_pages'], 4)
#         self.assertEqual(data['total_records'], 20)

#     def test_searchPatients(self):
#         url = reverse('search_patients')
#         response = self.client.get(url, {'name': 'John'})
#         self.assertEqual(response.status_code, 200)
#         # You can add more assertions to check the content of the response

#     def test_updatePatient(self):
#         # Create a patient to update
#         patient = Patient.objects.create(
#             patient_name="John Doe",
#             patient_phone_number="123-456-7890",
#             patient_address="123 Main St, City",
#             patient_gender="Male",
#             patient_date_of_birth="1990-01-15",
#             created_date_time=datetime.now(),
#             created_by_id=1,
#             last_updated_date_time=datetime.now(),
#             last_updated_id=1,
#             is_enabled=True,
#             remarks="This is a sample patient."
#         )

#         url = reverse('update_patient', args=[patient.pk])
#         data = {
#             "patient_name": "Updated John Doe",
#             "patient_phone_number": "987-654-3210",
#             "patient_address": "456 Elm St, Town",
#             "patient_gender": "Female",
#             "patient_date_of_birth": "1985-05-20",
#             "last_updated_id": 2,
#             "is_enabled": False,
#             "remarks": "Updated information."
#         }
#         response = self.client.put(url, json.dumps(
#             data), content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         # Check if the patient's information has been updated
#         updated_patient = Patient.objects.get(pk=patient.pk)
#         self.assertEqual(updated_patient.patient_name, "Updated John Doe")
#         self.assertEqual(updated_patient.patient_phone_number, "987-654-3210")
#         # Add more assertions to check other fields

#     # Add more test cases as needed for other views or edge cases
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Patient
from django.utils import timezone  # Import timezone
current_time = timezone.now()


class PatientTests(APITestCase):
    def setUp(self):

        self.patient_data = {
            "patient_name": "John Doe",
            "patient_phone_number": "123-456-7890",
            "patient_address": "123 Main St",
            "patient_gender": "Male",
            "patient_date_of_birth": "1990-01-01",
            "created_by_id": 1,
            "last_updated_id": 1,
            "created_date_time": current_time,
            "last_updated_date_time": current_time  # Set a valid timestamp here
        }

    def test_create_patient(self):
        url = reverse('add_patient')
        self.patient_data['created_date_time'] = str(timezone.now())
        response = self.client.post(url, self.patient_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)

    def test_get_patients(self):
        url = reverse('get_patients')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_patient(self):
        # Create a patient to update
        patient = Patient.objects.create(**self.patient_data)
        url = reverse('update_patient', args=[patient.patient_id])
        updated_data = {

            "patient_address": "123 Main St",
            "patient_gender": "Male",
            "patient_date_of_birth": "1990-01-01",
            "created_by_id": 1,
            "last_updated_id": 1,
            "created_date_time": current_time,
            "last_updated_date_time": current_time,
            "patient_name": "Updated Name",
            "patient_phone_number": "999-999-9999",
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        patient.refresh_from_db()
        self.assertEqual(patient.patient_name, "Updated Name")
        self.assertEqual(patient.patient_phone_number, "999-999-9999")


# sample json for data input add-patient
# [
#   {
#         "patient_name": "Jimmy",
#         "patient_phone_number": "5557778888",
#         "patient_address": "789 Oak Avenue, NYC",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Jenny Smith",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#     {
#         "patient_name": "John Snow",
#         "patient_phone_number": "5557778888",
#         "patient_address": "789 Oak Avenue, Moordale",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Jenna",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#       {
#         "patient_name": "Lauren ",
#         "patient_phone_number": "5557778888",
#         "patient_address": "789 Oak Avenue, Seaford",
#         "patient_gender": "female",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "David Smith",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#       {
#         "patient_name": "Kane ",
#         "patient_phone_number": "5557778888",
#         "patient_address": "789 Oak Avenue, Sunnydale",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Emily",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#       {
#         "patient_name": "Thomas Shelby",
#         "patient_phone_number": "5557778888",
#         "patient_address": "789 Oak Avenue, Birmingham",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Grace",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#       {
#         "patient_name": "Ella",
#         "patient_phone_number": "5557778888",
#         "patient_address": "789 Oak Avenue, Sunnydale",
#         "patient_gender": "female",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "David",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#       {
#         "patient_name": "Caitlyn",
#         "patient_phone_number": "5557778888",
#         "patient_address": "789 Oak Avenue,Oklahoma",
#         "patient_gender": "female",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Barron",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#       {
#         "patient_name": "George",
#         "patient_phone_number": "5557778888",
#         "patient_address": "4709 S poplar Ave Broken Arrow, OK 74011",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Alison",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#       {
#         "patient_name": "Henry",
#         "patient_phone_number": "5557778888",
#         "patient_address": "4709 S poplar Ave Broken Arrow, OK 74011",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Sky",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#     {
#         "patient_name": "Kevin",
#         "patient_phone_number": "5557778888",
#         "patient_address": "4709 S poplar Ave Broken Arrow, OK 74011",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Sky",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#     {
#         "patient_name": "David",
#         "patient_phone_number": "5557778888",
#         "patient_address": "4709 S poplar Ave Broken Arrow, OK 74011",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Sky",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#     {
#         "patient_name": "Mitchell",
#         "patient_phone_number": "5557778888",
#         "patient_address": "4709 S poplar Ave Broken Arrow, OK 74011",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Sky",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#     {
#         "patient_name": "Abraham",
#         "patient_phone_number": "5557778888",
#         "patient_address": "4709 S poplar Ave Broken Arrow, OK 74011",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Sky",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#     {
#         "patient_name": "Noah",
#         "patient_phone_number": "5557778888",
#         "patient_address": "4709 S poplar Ave Broken Arrow, OK 74011",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Sky",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#     {
#         "patient_name": "Harry Styles",
#         "patient_phone_number": "5557778888",
#         "patient_address": "4709 S poplar Ave Broken Arrow, OK 74011",
#         "patient_gender": "male",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "Sky",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
#     {
#         "patient_name": "Selena",
#         "patient_phone_number": "5557778888",
#         "patient_address": "4709 S poplar Ave Broken Arrow, OK 74011",
#         "patient_gender": "female",
#         "patient_date_of_birth": "1992-03-12",
#         "patient_guardian": "john",
#         "created_date_time": "2023-10-11T08:15:00",
#         "created_by_id": 3,
#         "last_updated_date_time": "2023-10-11T08:15:00",
#         "last_updated_id": 3,
#         "is_enabled": true,
#         "remarks": "New patient entry"
#     },
# ]
