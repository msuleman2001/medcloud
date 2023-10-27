from django.urls import path

from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('all', addDoctor.as_view(), name="doctors"),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('doclogin/', DoctorLoginView.as_view(), name='doctor_login'),
    # path('doctors/', getDoctors.as_view(), name="getDoctors"),

    # path('update/', updateDoctor.as_view(), name="updateDoctor"),

]