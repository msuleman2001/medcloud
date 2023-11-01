from rest_framework import serializers
from .models import Manager


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'  # This will include all fields in the Manager model
