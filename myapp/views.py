from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView,\
CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cars
from .seriallizers import CarsSerializer


    

class CarsDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        car = Cars.objects.filter(pk=pk).first()
        if car:
            serializer = CarsSerializer(car)
            data = {
                'status': status.HTTP_200_OK,
                'message': 'Maxsulot',
                'product': serializer.data
            }
            return Response(data)
        data = {
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'Maxsulot topilmadi',
        }
        return Response(data)
    
    def put(self, request, pk):
        car = Cars.objects.filter(pk=pk).first()
        if car:
            serializer = CarsSerializer(car, data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = {
                    'status': status.HTTP_200_OK,
                    'message': 'Maxsulot yangilandi',
                    'product': serializer.data
                }
                return Response(data)
            data = {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Maxsulot yangilanmadi',
                'error': serializer.errors
            }
            return Response(data)
        data = {
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'Maxsulot topilmadi',
        }
        return Response(data)
    
    def delete(self, request, pk):
        car = Cars.objects.filter(pk=pk).first()
        if car:
            car.delete()
            data = {
                'status': status.HTTP_200_OK,
                'message': 'Maxsulot ochirildi',
            }
            return Response(data)
        data = {
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'Maxsulot topilmadi',
        }
        return Response(data)
    
    
class CarsListCreateView(APIView):
    def get(self, request):
        cars = Cars.objects.all()
        serializer = CarsSerializer(cars, many=True)
        data = {
            'status': status.HTTP_200_OK,
            'message': 'Maxsulotlar ro`yxati',
            'products': serializer.data
        }
        return Response(data)
    def post(self, request):
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'message': 'Maxsulot yaratildi',
                'product': serializer.data
            }
            return Response(data)
        data = {
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Maxsulot yaratilmadi',
            'error': serializer.errors
        }
        return Response(data)
    

















