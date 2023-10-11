from django.urls import path
from . import views

urlpatterns = [
    path('all', views.addDoctor, name="doctors"),
    path('doctors/', views.getDoctors, name="getDoctors"),

    path('update/', views.updateDoctor, name="updateDoctor"),
]