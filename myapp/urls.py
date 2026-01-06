from django.urls import path
# from .views import CarsListCreateView, CarsRetrieveUpdateDestroyView
from .views import CarsListview, CarsCreateView, CarsRetrieveView, CarsUpdateView, CarsDestroyView
urlpatterns = [
    # path('list-create/', CarsListCreateView.as_view()),
    # path('retrieve-update-destroy/<int:pk>/', CarsRetrieveUpdateDestroyView.as_view())
    path('list/', CarsListview.as_view()),
    path('create/', CarsCreateView.as_view()),
    path('retrieve/<int:pk>/', CarsRetrieveView.as_view()),
    path('update/<int:pk>/', CarsUpdateView.as_view()),
    path('destroy/<int:pk>/', CarsDestroyView.as_view()),
]