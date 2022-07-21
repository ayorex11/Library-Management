from django.urls import path
from . import views

urlpatterns = [
	path("addresses/", views.ListAddressAPIView.as_view()),
    path("address/<int:pk>", views.AddressDetailView.as_view()),
    path("create/address/", views.createAddressAPIView.as_view()),
]