from django.urls import path
from . import views

urlpatterns= [
    path('students/', views.students),
    path('students/<int:pk>/', views.student_details),
    path('employees/', views.Employees.as_view())
    path('students/<int:pk>/', views.EmployeeDetails.as_view())
]