from rest_framework import serializers
from .models import Museumtual 

class MuseumtualSerializer(serializers.ModelSerializer): #take the object to the database
    class Meta: 
        model = Museumtual
        fields = '__all__'