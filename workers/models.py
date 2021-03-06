# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Departments(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'

    def __str__(self):
        return self.dept_name


class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    job_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'

    def __str__(self):
        return self.job_title


class Employees(models.Model):
    emp_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    hire_date = models.DateField(db_column='Hire_date', blank=True, null=True)  # Field name made lowercase.
    job = models.ForeignKey('Jobs', models.DO_NOTHING, db_column='Job_Id', blank=True,
                            null=True)  # Field name made lowercase.
    salary = models.IntegerField(blank=True, null=True)
    commision_pct = models.FloatField(blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'

    def __str__(self):
        return self.emp_id

