from django.urls import path 
from . import views 

urlpatterns = [
	path('create/<str:pk>/', views.create_cart),
	path('get_cart/', views.get_cart),
]