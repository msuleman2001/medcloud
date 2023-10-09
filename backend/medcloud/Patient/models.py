from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=255)
    patient_phone_number = models.CharField(max_length=15)
    patient_address = models.TextField()
    patient_gender = models.CharField(max_length=10)
    patient_date_of_birth = models.DateField()
    patient_guardian = models.CharField(max_length=255, null=True, blank=True)
    created_date_time = models.DateTimeField()
    created_by_id = models.IntegerField()
    last_updated_date_time = models.DateTimeField()
    last_updated_id = models.IntegerField()
    is_enabled = models.BooleanField(default=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.patient_name
