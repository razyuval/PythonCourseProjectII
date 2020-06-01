from rest_framework import serializers
from .models import Jobs, Employees, Departments


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('job_id', 'job_title', 'job_desc')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('emp_id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'job', 'salary', 'commision_pct', 'manager_id', 'department')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('dept_id', 'dept_name')

