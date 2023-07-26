from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from .models import Museumtual
from .models import Book
from .serializers import MuseumtualSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import BookSerializer
from rest_framework.response import Response
from .serializers import CartSerializer
from .models import Cart
import requests
from rest_framework.response import Response 


from .models import Museum
from .serializers import MuseumSerializer



import os

print(str(os.getenv('API_KEY')))
# Create your views here.

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer      

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class MuseumtualListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Museumtual.objects.all()
    serializer_class = MuseumtualSerializer

class MuseumtualDeleteView(DestroyAPIView):
    queryset = Museumtual.objects.all()
    serializer_class = MuseumtualSerializer

class MuseumtualUpdateView(UpdateAPIView):
    queryset = Museumtual.objects.all()
    serializer_class = MuseumtualSerializer


class MuseumtualRetrieveView(RetrieveAPIView):
    queryset = Museumtual.objects.all()
    serializer_class = MuseumtualSerializer     

class MuseumtualCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]       

#  view post request
    def post(self, request):
        user = request.user
        print(user)
        data = request.data
        data['owner'] = user.id
        print(data)
        serializer = MuseumtualSerializer(data=data)

        # checks serializer has all of the data it needs
        if serializer.is_valid():

        # then save it to the databace    
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(None, status=200)
    
    
class MuseumtualListView(ListAPIView):
    def get_queryset(self):
        user = self.request.user
        return Museumtual.objects
    serializer_class = MuseumtualSerializer



class CartCreateView:
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
   
    
     
class CartListView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDeleteView(DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartUpdateView(UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
from django.http import HttpResponse, JsonResponse

def get_exhibition(request):
    payload = {'apikey': f'7f655026-78b4-4e35-be48-e3688920438c'}
    r = requests.get('https://api.harvardartmuseums.org/exhibition', params=payload)
    return JsonResponse({"message":r.json()})





class MuseumListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer


class MuseumCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

#Method will run when the view get a post request
    def post(self, request):
        user = request.user
        print(user)
        data = request.data
        data['owner'] = user.id
        print(data)
        serializer = MuseumSerializer(data=data)
        # checks rather har serializer has all of the data it needs
        if serializer.is_valid():
        # save that data to the databace    
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(None, status=200)


class MuseumListview(ListAPIView):
    def get_queryset(self):
        user = self.request.user
        return Museum.objects.filter(owner = user)
    
    serializer_class = MuseumSerializer



class MuseumDeleteView(DestroyAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer
