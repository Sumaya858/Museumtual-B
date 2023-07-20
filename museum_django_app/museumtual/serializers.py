from rest_framework import serializers
from .models import Museumtual 
from .models import Profile
from .models import Cart

class MuseumtualSerializer(serializers.ModelSerializer): #take the object to the database
    class Meta: 
        model = Museumtual
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer): #take the object to the database
    class Meta: 
        model = Profile
        fields = '__all__'    


class CartSerializer(serializers.ModelSerializer): #take the object to the database
    class Meta: 
        model = Cart
        fields = '__all__'      