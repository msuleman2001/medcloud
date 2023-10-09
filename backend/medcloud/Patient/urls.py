from django.urls import path
from . import views

urlpatterns = [
    path('patientlist', views.getPatient, name="getPatient"),
]
