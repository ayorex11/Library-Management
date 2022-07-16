from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer, CategorySerializer
from .models import Book, Category


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def book_list(request):

	book = Book.objects.filter(available=True)
	serializer = BookSerializer(book, many=True)

	data ={'message': 'success',
			'data': serializer.data}

	return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])

def category_list(request):

	category = Category.objects.all()
	serializer = CategorySerializer(category, many=True)

	data = {'message': 'success',
			'data': serializer.data}

	return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])

def book_detail(request, pk):

	books = Book.objects.get(id=pk)
	serializer = BookSerializer(books, many=False)

	data = {'message': 'success',
			'data': serializer.data}

	return Response(data=data, status=status.HTTP_200_OK)
