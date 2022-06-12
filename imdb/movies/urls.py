from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.movie_list, name='list'),
    path('<slug:slug>/', views.movie_detail, name='detail'),



]
