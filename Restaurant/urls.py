from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.restaurant_new),
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]