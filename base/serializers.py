from rest_framework import serializers
from .models import Doctor,Appointment


class DoctorSerlizer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'


class AppointmentSerlizer(serializers.ModelSerializer):
    # doctor=serializers.StringRelatedField()
    # patient=serializers.StringRelatedField()
    class Meta:
        model = Appointment
        fields = '__all__'