from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import RentageSerializer, CartBookSerializer, RentageMiniSerializer, RentageUpdateSerializer
from main.models import Book
from .models import Rentage
from django.shortcuts import get_object_or_404 
from drf_yasg.utils import swagger_auto_schema



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def create_cart(request, pk):
	User = request.user 
	book =  get_object_or_404(Book, id=pk)
	total = book.price 
	cart = Rentage(user=User, books=book, total=total)
	cart.save()
	serializer = RentageSerializer(cart)
	data ={'message': 'book successfully added',
			'data':serializer.data}
	return Response(data=data, status=status.HTTP_200_OK)





