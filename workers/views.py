from django.shortcuts import render, redirect
from .models import Departments, Employees, Jobs
from .serializers import DepartmentSerializer, JobSerializer, EmployeeSerializer
from rest_framework import viewsets, permissions


def WorkersView(request):
    workers=Employees.objects.all
    return render(request, 'workers.html', {'workers': workers})


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
   # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class JobView(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer


class DepartmentView(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer

