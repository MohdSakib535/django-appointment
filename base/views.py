from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Doctor, Appointment
from .serializers import DoctorSerlizer,AppointmentSerlizer

class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerlizer
    # permission_classes = [permissions.IsAuthenticated]

class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerlizer
    # permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)