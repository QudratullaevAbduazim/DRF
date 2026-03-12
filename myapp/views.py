from django.shortcuts import render


from rest_framework import viewsets
from .models import Products
from .serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
