from django.contrib import admin
from .models import Departments
from .models import Employees
from .models import Jobs



admin.site.register(Departments)
admin.site.register(Employees)
admin.site.register(Jobs)
