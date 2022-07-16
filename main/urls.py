from django.urls import path 
from . import views

urlpatterns = [
	path('book/', views.book_list),
	path('category/', views.category_list),
	path('bookdetail/<str:pk>/', views.book_detail),

]