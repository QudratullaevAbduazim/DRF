from django.urls import path
from myapp2.views import ListCreateView, UpdateDeleteDetailView
urlpatterns = [
    # path('products/', ProductListView.as_view()),
    # path('product/<int:pk>/', ProductDetailView.as_view()),
    path('list/create/', ListCreateView.as_view()),
    path('update/delete/detail<int:pk>/', UpdateDeleteDetailView.as_view()),
    # path('product/delete/<int:pk>/', ProductDeleteView.as_view()),
]