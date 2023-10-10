from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse
from .models import Doctor
import json

class DoctorViewTestCase(TestCase):
    def test_add_doctor(self):
        # Define the data for the new doctor to be added
        new_doctor_data = {
            'name': 'New Doctor',
            'email': 'newdoctor@example.com',
            'phone': '987-654-3210',
            'license': '54321',  # Corrected key to 'license'
            'speciality': 'Neurology',
            'start_year': 2010,
            'clinic_address': '789 Elm St',
            'added_by_id': 3,
            'remarks': 'Test remarks for New Doctor'
        }

        # Create a JSON string from the new doctor data
        new_doctor_data_json = json.dumps(new_doctor_data)

        # Test the addDoctor view by making a POST request
        url = reverse('doctors')  # Assuming you have defined a URL pattern with the name 'doctors'
        response = self.client.post(url, data=new_doctor_data_json, content_type='application/json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected message
        expected_response = {'message': 'Doctor added successfully'}
        self.assertEqual(response.json(), expected_response)

        # Verify that the new doctor has been added to the database
        new_doctor = Doctor.objects.get(name='New Doctor')
        self.assertIsNotNone(new_doctor)
        # Add more assertions to verify the data of the new doctor if needed
    
    
    
    
    
    def setUp(self):
        # Create some sample doctors for testing
        self.doctor1 = Doctor.objects.create(
            email='doctor1@example.com',
            name='Doctor One',
            phone='123-456-7890',
            license_no='12345',
            speciality='Cardiology',
            start_year=2000,
            clinic_address='123 Main St',
            country='USA',
            added_by_id=1,
            added_datetime="2023-10-06 08:05:45.691956",
            last_update_date_time="2023-10-07 07:04:58.167356",
            remarks='Test remarks for Doctor One',
            is_enabled=True,
        )

        self.doctor2 = Doctor.objects.create(
            email='doctor2@example.com',
            name='Doctor Two',
            phone='987-654-3210',
            license_no='54321',
            speciality='Dermatology',
            start_year=2005,
            clinic_address='456 Elm St',
            country='Canada',
            added_by_id=2,
            is_enabled=False,
            remarks='Test remarks for Doctor Two'
        )

    def test_get_doctors(self):
        # Test the getDoctors view by making a GET request
        url = reverse('getDoctors')  # Assuming you have defined a URL pattern with the name 'get_doctors'
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Deserialize the JSON response
        response_data = response.json()

        # Check if the 'doctors' key exists in the response
        self.assertIn('doctors', response_data)

        # Check if the response contains the expected number of doctors
        self.assertEqual(len(response_data['doctors']), 2)

        # Check if the response data for the first doctor matches the expected data
        self.assertEqual(response_data['doctors'][0]['name'], 'Doctor One')
        self.assertEqual(response_data['doctors'][0]['phone'], '123-456-7890')
        self.assertEqual(response_data['doctors'][0]['license_no'], '12345')
        self.assertEqual(response_data['doctors'][0]['speciality'], 'Cardiology')
        self.assertEqual(response_data['doctors'][0]['start_year'], 2000)
        self.assertEqual(response_data['doctors'][0]['clinic_address'], '123 Main St')
        self.assertEqual(response_data['doctors'][0]['country'], 'USA')
        self.assertEqual(response_data['doctors'][0]['added_by_id'], 1)
        self.assertEqual(response_data['doctors'][0]['is_enabled'], True)
        self.assertEqual(response_data['doctors'][0]['remarks'], "Test remarks for Doctor One")

        # Add more assertions for other fields as needed

        # Check if the response data for the second doctor matches the expected data
        self.assertEqual(response_data['doctors'][1]['name'], 'Doctor Two')
        self.assertEqual(response_data['doctors'][1]['speciality'], 'Dermatology')
        # Add more assertions for other fields as needed