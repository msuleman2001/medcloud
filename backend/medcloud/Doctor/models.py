from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models

class Doctor(AbstractUser):
    email = models.EmailField()
    phone = models.CharField(max_length=20, unique=True)  # Ensure phone is unique and used as the username
    
    license_no = models.CharField(max_length=54)
    speciality = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField()
    clinic_address = models.TextField()
    country = models.CharField(max_length=50)
    added_by_id = models.PositiveIntegerField()
    added_datetime = models.DateTimeField(auto_now_add=True)
    last_update_date_time = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=False)
    remarks = models.TextField()
    # USERNAME_FIELD = 'phone'  # Set the phone field as the username field

    def get_username(self):
        return self.phone  # Return the phone as the username


    def __str__(self):
        return self.name