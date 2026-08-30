from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    home_view, 
    programmers_list_view, 
    sistemas_list_view,
    ProgrammerViewSet,
    SistemaViewSet,
    ProgrammerListAPIView,
    SistemaListAPIView
)

# Configuración del Router para los ViewSets
router = DefaultRouter()
router.register(r'programmers', ProgrammerViewSet, basename='programmer')
router.register(r'sistemas', SistemaViewSet, basename='sistema')

urlpatterns = [
    # Rutas de vistas Web HTML
    path('', home_view, name='home'),
    path('programadores-web/', programmers_list_view, name='programmers-list-html'),
    path('programadores_web/', programmers_list_view),
    path('sistemas-web/', sistemas_list_view, name='sistemas-list-html'),
    path('sistemas_web/', sistemas_list_view),

    # Endpoints de la API REST generados por el Router (/api/programmers/ y /api/sistemas/)
    path('api/', include(router.urls)),

    # Endpoints personalizados para APIViews con soporte de filtro ?q=
    path('api/programmers-list/', ProgrammerListAPIView.as_view(), name='programmers-list-api'),
    path('api/sistemas-list/', SistemaListAPIView.as_view(), name='sistemas-list-api'),
]