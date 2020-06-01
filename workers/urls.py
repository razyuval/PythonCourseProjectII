from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('Employee', views.EmployeeView, basename='Workers')
router.register('Job', views.JobView, basename='Jobs')
router.register('Department', views.DepartmentView, basename='Departments')

urlpatterns = [
    path('', views.WorkersView),
    path('data/', include(router.urls))
]



