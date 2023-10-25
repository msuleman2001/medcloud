from rest_framework import serializers
from .models import Doctor
# class DoctorSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Doctor
#     fields = '__all__'

class DoctorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Doctor
        fields = ('email', 'phone', 'username', 'first_name','last_name', 'license_no', 'speciality', 'start_year', 'clinic_address', 'country', 'added_by_id', 'remarks', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        doctor = Doctor(**validated_data)
        doctor.set_password(password)
        doctor.save()
        return doctor
    
class DoctorLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)