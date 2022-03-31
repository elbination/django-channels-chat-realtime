from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_rooms, name='room-list'),
    path('<slug:slug>/', views.get_room, name='room-detail'),
]
