from django.test import TestCase
from django.urls import reverse
from .models import Patient
import json
from datetime import datetime


class PatientViewsTest(TestCase):

    def test_addPatient(self):
        url = reverse('add_patient')
        data = {
            "patient_name": "John Doe",
            "patient_phone_number": "123-456-7890",
            "patient_address": "123 Main St, City",
            "patient_gender": "Male",
            "patient_date_of_birth": "1990-01-15",
            "created_date_time": datetime.now().isoformat(),
            "created_by_id": 1,
            "last_updated_date_time": datetime.now().isoformat(),
            "last_updated_id": 1,
            "is_enabled": True,
            "remarks": "This is a sample patient."
        }
        response = self.client.post(url, json.dumps(
            data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Patient.objects.count(), 1)

    def test_getPatients(self):
        url = reverse('get_patients')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # You can add more assertions to check the content of the response

    def test_searchPatients(self):
        url = reverse('search_patients')
        response = self.client.get(url, {'name': 'John'})
        self.assertEqual(response.status_code, 200)

    def test_updatePatient(self):
        # Create a patient to update
        patient = Patient.objects.create(
            patient_name="John Doe",
            patient_phone_number="123-456-7890",
            patient_address="123 Main St, City",
            patient_gender="Male",
            patient_date_of_birth="1990-01-15",
            created_date_time=datetime.now(),
            created_by_id=1,
            last_updated_date_time=datetime.now(),
            last_updated_id=1,
            is_enabled=True,
            remarks="This is a sample patient."
        )

        url = reverse('update_patient', args=[patient.pk])
        data = {
            "patient_name": "Updated John Doe",
            "patient_phone_number": "987-654-3210",
            "patient_address": "456 Elm St, Town",
            "patient_gender": "Female",
            "patient_date_of_birth": "1985-05-20",
            "last_updated_id": 2,
            "is_enabled": False,
            "remarks": "Updated information."
        }
        response = self.client.put(url, json.dumps(
            data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Check if the patient's information has been updated
        updated_patient = Patient.objects.get(pk=patient.pk)
        self.assertEqual(updated_patient.patient_name, "Updated John Doe")
        self.assertEqual(updated_patient.patient_phone_number, "987-654-3210")
    # Add more test cases as needed for other views or edge cases


# {
#     "patient_name": "Abu Zain",
#     "patient_phone_number": "123-456-7890",
#     "patient_address": "123 Main St, BWP City",
#     "patient_gender": "Male",
#     "patient_date_of_birth": "1990-01-15",
#     "patient_guardian": "Jane Doe",
#     "created_date_time": "2023-10-09T12:00:00Z",
#     "created_by_id": 1,
#     "last_updated_date_time": "2023-10-09T12:00:00Z",
#     "last_updated_id": 1,
#     "is_enabled": true,
#     "remarks": "This is a sample patient."
# }
