"""
URL configuration for IEC_N4_C2_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for IEC_N4_C2_backend project.
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.views import login_view, home_view, teachers_view, courses_view, students_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. RUTA DE LOGIN PERSONALIZADO
    path('login/', login_view, name='login'),
    
    # 2. RUTAS FRONTEND
    path('', home_view, name='home'),
    path('teachers/', teachers_view, name='teachers_list'),
    path('teachers/', teachers_view, name='teachers-list-html'),
    path('courses/', courses_view, name='courses_list'),
    path('courses/', courses_view, name='courses-list-html'),
    path('students/', students_view, name='students_list'),
    path('students/', students_view, name='students-list-html'),

    # 3. ENDPOINTS API REST Y JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # 4. REGISTRO OBLIGATORIO DEL NAMESPACE DE DRF (Soluciona el error actual)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 5. RUTAS DE TU API REST
    path('api/', include('api.urls')),
]