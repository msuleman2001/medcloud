from django.urls import path

from .views import *


urlpatterns = [
    path('all', addDoctor.as_view(), name="doctors"),
    path('doclogin/', DoctorLoginView.as_view(), name='doctor-login'),
    # path('doctors/', getDoctors.as_view(), name="getDoctors"),

    # path('update/', updateDoctor.as_view(), name="updateDoctor"),
]