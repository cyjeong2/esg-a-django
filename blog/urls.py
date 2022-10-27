from django.urls import path
from blog import views

urlpatterns = [
    path('new/', views.post_new),
    path('', views.index), 
    path('<int:pk>/', views.single_post_page),
]
