from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ['created_at']

class MappingSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(), source='doctor', write_only=True
    )

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'doctor_id', 'assigned_at']
        read_only_fields = ['assigned_at']
