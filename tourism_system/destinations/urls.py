from django.urls import path
from . import views

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('create/', views.destination_create, name='destination_create'),
    path('<int:pk>/update/', views.destination_update, name='destination_update'),
    path('<int:pk>/delete/', views.destination_delete, name='destination_delete'),
]
