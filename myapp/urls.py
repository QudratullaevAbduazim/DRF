from django.urls import path
# from .views import CarsListCreateView, CarsRetrieveUpdateDestroyView
from .views import  CarsDetailUpdateDeleteView #CarsCreateListView #DeleteView, UpdateView CarsListview, CarsCreateView, CarsRetrieveView, CarsUpdateView, CarsDestroyView, 
urlpatterns = [
    # path('list-create/', CarsCreateListView.as_view()),
    path('detail-update-delete/<int:pk>/', CarsDetailUpdateDeleteView.as_view())
    # path('list/', CarsListview.as_view()),
    # path('create/', CarsCreateView.as_view()),
    # path('retrieve/<int:pk>/', CarsRetrieveView.as_view()),
    # path('update/<int:pk>/', CarsUpdateView.as_view()),
    # path('destroy/<int:pk>/', DeleteView.as_view()),
    # path('update/<int:pk>/', UpdateView.as_view())
]