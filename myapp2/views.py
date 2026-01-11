from django.shortcuts import render
from rest_framework import status
# from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Products
from .serializer import ProductsSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ValidationError
from myapp2 import serializer

    


class ListCreateView(GenericAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            'status': status.HTTP_200_OK,
            'data': serializer.data,
            'count': len(serializer.data)
        }
        return Response(data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
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
    
    
    


    


class UpdateDeleteDetailView(GenericAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

    def get_object(self, pk):

        try:
            return Products.objects.get(pk=pk)
        
        except Products.DoesNotExist:
            data = {
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Maxsulot topilmadi',
            }
            raise ValidationError(data)
    
    def get(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = self.get_serializer(product)
        if product:
            serializer = ProductsSerializer(product)
            data = {
                'status': status.HTTP_200_OK,
                'message': 'Maxsulot',
                'product': serializer.data
            }
            return Response(data)
        

        def delete(self, request, pk):
            product = self.get_object(pk=pk)
        if product:
            product.delete()
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


    def put(self, request, pk):
        product = self.get_object(pk=pk)
        if product:
            serializer = ProductsSerializer(product, data=request.data, partial=True)
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

    def patch(self, request, pk):
        product = self.get_object(pk=pk)
        if product:
            serializer = ProductsSerializer(product, data=request.data, partial=True)
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