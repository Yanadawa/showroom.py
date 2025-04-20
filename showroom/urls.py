from django.urls import path
from . import views
from .views import CarDeleteView

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('cars/add/', views.car_add, name='car_add'),
    path('cars/<int:car_id>/service/', views.service_add, name='service_add'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
]
