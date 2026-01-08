from django.urls import path
from myapp2.views import ProductCreateView, ProductDeleteView, ProductDetailView, ProductListView, ProductUpdate
urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('product/create/', ProductCreateView.as_view()),
    path('product/update/<int:pk>/', ProductUpdate.as_view()),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view()),
]