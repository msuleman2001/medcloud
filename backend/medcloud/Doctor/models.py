from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

# Create your models here.
from django.db import models

class Doctor(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    license_no = models.CharField(max_length=50)
    speciality = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField()
    clinic_address = models.TextField()
    country = models.CharField(max_length=50)
    added_by_id = models.PositiveIntegerField()
    added_datetime = models.DateTimeField(auto_now_add=True)
    last_update_date_time = models.DateTimeField(auto_now=True)
    remarks = models.TextField()

    def __str__(self):
        return self.name