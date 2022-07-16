from rest_framework import serializers
from main.models import Book
from .models import Rentage


class CartBookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['name', 'description', 'ISBN', 'price']


class RentageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rentage
		fields = ['user', 'books', 'total']

class RentageMiniSerializer(serializers.ModelSerializer):
	

	class Meta:
		model = Rentage
		fields = ['books',]


class RentageUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rentage
		fields = ['books',]