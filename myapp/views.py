from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView,\
CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Cars
from .seriallizers import CarsSerializer

# Create your views here.

# class CarsListCreateView(ListCreateAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer

# class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer
#     lookup_field = 'pk'



class CarsListview(ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class CarsCreateView(CreateAPIView):   
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class CarsRetrieveView(RetrieveAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    lookup_field = 'pk'

class CarsUpdateView(UpdateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    lookup_field = 'pk'

class CarsDestroyView(DestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    lookup_field = 'pk'

