from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from .models import Teacher, Course, Student, StudentCourse
from .serializer import (
    TeacherSerializer, CourseSerializer,
    StudentSerializer, StudentCourseSerializer
)

# --- REST API ViewSets ---
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer

# --- Vistas HTML ---
def home_view(request):
    return render(request, 'index.html')

@login_required(login_url='rest_framework:login')
def teachers_view(request):
    return render(request, 'teachers_list.html')

@login_required(login_url='rest_framework:login')
def courses_view(request):
    return render(request, 'courses_list.html')

@login_required(login_url='rest_framework:login')
def students_view(request):
    return render(request, 'students_list.html')


