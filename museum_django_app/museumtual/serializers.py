from rest_framework import serializers
from .models import Museumtual 
from .models import Book
from .models import Cart
from .models import Museum

class MuseumtualSerializer(serializers.ModelSerializer): #take the object to the database
    class Meta: 
        model = Museumtual
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer): #take the object to the database
    class Meta: 
        model = Book
        fields = '__all__'    


class CartSerializer(serializers.ModelSerializer): #take the object to the database
    class Meta: 
        model = Cart
        fields = '__all__'      


class MuseumSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Museum
        fields = '__all__'      