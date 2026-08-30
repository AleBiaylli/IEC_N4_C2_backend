from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import programmer, Sistema
from .serializer import ProgrammerSerializer, SistemaSerializer


# --- Vistas Web HTML ---

def home_view(request):
    return render(request, 'index.html')


@login_required(login_url='rest_framework:login')
def programmers_list_view(request):
    query = request.GET.get('q', '')
    if query:
        programmers = programmer.objects.filter(Nombre__icontains=query)
    else:
        programmers = programmer.objects.all()
        
    return render(request, 'programmers_list.html', {'programmers': programmers})


@login_required(login_url='rest_framework:login')
def sistemas_list_view(request):
    query = request.GET.get('q', '')
    if query:
        sistemas = Sistema.objects.filter(nombre_sistema__icontains=query)
    else:
        sistemas = Sistema.objects.all()
        
    return render(request, 'sistemas_list.html', {'sistemas': sistemas})


def api_root_redirect(request):
    return redirect('programmer-list')


# --- Vistas API REST (ViewSets para Router) ---

class ProgrammerViewSet(viewsets.ModelViewSet): 
    queryset = programmer.objects.all() 
    serializer_class = ProgrammerSerializer


class SistemaViewSet(viewsets.ModelViewSet):
    queryset = Sistema.objects.all()
    serializer_class = SistemaSerializer


# --- Vistas API REST (APIViews personalizadas) ---

class ProgrammerListAPIView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            programmers = programmer.objects.filter(Nombre__icontains=query)
        else:
            programmers = programmer.objects.all()
            
        serializer = ProgrammerSerializer(programmers, many=True)
        return Response(serializer.data)


class SistemaListAPIView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            sistemas = Sistema.objects.filter(nombre_sistema__icontains=query)
        else:
            sistemas = Sistema.objects.all()
            
        serializer = SistemaSerializer(sistemas, many=True)
        return Response(serializer.data)