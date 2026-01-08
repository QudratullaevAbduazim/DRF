from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Products
from .serializer import ProductsSerializer
# Create your views here.

class ProductListView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        data = {
            'status': status.HTTP_200_OK,
            'message': 'Maxsulotlar royhati',
            'Soni': len(products),
            'products': serializer.data
        }
        return Response(data)
    

class ProductDetailView(APIView):
    def get(self, request, pk):
        product = Products.objects.filter(pk=pk).first()
        if product:
            serializer = ProductsSerializer(product)
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
    

class ProductCreateView(APIView):
    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
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
    
class ProductUpdate(APIView):
    def put(self, request, pk):
        product = Products.objects.filter(pk=pk).first()
        if product:
            serializer = ProductsSerializer(product, data=request.data)
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
    
class ProductDeleteView(APIView):
    def delete(self, request, pk):
        product = Products.objects.filter(pk=pk).first()
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
    

