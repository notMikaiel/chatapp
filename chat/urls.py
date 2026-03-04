from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('<str:room_name>/', views.room_detail, name='room_detail'),
]