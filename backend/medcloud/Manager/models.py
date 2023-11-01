from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


class Manager(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)
    cnic_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    photograph = models.ImageField(
        upload_to='manager_photos/', null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    created_by_id = models.PositiveIntegerField()
    last_update_date_time = models.DateTimeField(auto_now=True)
    last_updated_by_id = models.PositiveIntegerField()
    is_enabled = models.BooleanField(default=False)

    def get_username(self):
        return self.phone

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    groups = models.ManyToManyField(
        Group,
        related_name='managers',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='manager_permissions',
        blank=True,
    )
