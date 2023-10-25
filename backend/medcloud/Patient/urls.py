# from django.urls import path
# from . import views

# urlpatterns = [
#     # Add a new patient
#     path('add-patient/', views.addPatient, name='add_patient'),

#     # Get a list of all patients
#     path('get-patients/', views.getPatients, name='get_patients'),

#     # Search patients based on filters (implement your logic)
#     path('search-patients/', views.searchPatients, name='search_patients'),

#     # Update an existing patient
#     path('update-patient/<int:patient_id>/',
#          views.updatePatient, name='update_patient'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('add_patient/', views.add_patient, name='add_patient'),
    path('get_patients/', views.get_patients, name='get_patients'),
    path('search_patients/', views.search_patients, name='search_patients'),
    path('update_patient/<int:patient_id>/',
         views.update_patient, name='update_patient'),
]
