from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuItem, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['BookingDate', 'first_name', 'id', 'no_of_guest']

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']