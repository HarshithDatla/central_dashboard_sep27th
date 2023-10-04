from django.shortcuts import render

# Create your views here.
# dashboard/views.py
from rest_framework import generics
from .models import Trust, School
from .serializers import TrustSerializer, SchoolSerializer

from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.decorators import login_required

class TrustList(generics.ListCreateAPIView):
    serializer_class = TrustSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add appropriate permission classes

    def get_queryset(self):
        # Get the authenticated user
        user = self.request.user

        # Filter trusts based on the user's trust
        trusts = Trust.objects.filter(user=user)

        return trusts


# class TrustDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Trust.objects.all()
#     serializer_class = TrustSerializer
class TrustDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trust.objects.all()
    serializer_class = TrustSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add appropriate permission classes

    def get_queryset(self):
        # Get the authenticated user
        user = self.request.user

        # Filter trusts based on the user's trust
        trusts = Trust.objects.filter(user=user)

        return trusts

class SchoolList(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add appropriate permission classes

    def get_queryset(self):
        # Get the authenticated user
        user = self.request.user

        # Filter schools based on the user's trust
        trusts = Trust.objects.filter(user=user)
        schools = School.objects.filter(trust__in=trusts)

        return schools


# class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add appropriate permission classes

    def get_queryset(self):
        # Get the authenticated user
        user = self.request.user

        # Filter schools based on the user's trust
        trusts = Trust.objects.filter(user=user)
        schools = School.objects.filter(trust__in=trusts)

        return schools

    




