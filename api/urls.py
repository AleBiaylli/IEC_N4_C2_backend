from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home_view, teachers_view, courses_view, students_view,
    TeacherViewSet, CourseViewSet, StudentViewSet, StudentCourseViewSet
)

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'student-courses', StudentCourseViewSet, basename='studentcourse')

urlpatterns = [
    # Rutas Web HTML
    path('', home_view, name='home'),
    path('teachers-web/', teachers_view, name='teachers-list-html'),
    path('courses-web/', courses_view, name='courses-list-html'),
    path('students-web/', students_view, name='students-list-html'),

    # Endpoints REST API
    path('api/', include(router.urls)),
]