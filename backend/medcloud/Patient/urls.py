from django.urls import path
from . import views

urlpatterns = [
    # Add a new patient
    path('add-patient/', views.addPatient, name='add_patient'),

    # Get a list of all patients
    path('get-patients/', views.getPatients, name='get_patients'),

    # Search patients based on filters (implement your logic)
    path('search-patients/', views.searchPatients, name='search_patients'),

    # Update an existing patient
    path('update-patient/<int:patient_id>/',
         views.updatePatient, name='update_patient'),
]
