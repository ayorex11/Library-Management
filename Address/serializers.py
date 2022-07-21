from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['country', 'city', 'user', 'district', 'street_address', 'postal_code', 'building_number', 'apartment_number']


class CreateAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ["primary", "user"]

class ListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = ['country', 'city', 'user', 'primary']