from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from .models import Museumtual
from .serializers import MuseumtualSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

# Create your views here.

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
            return Museumtual.objects.filter(owner = user)
        serializer_class = MuseumtualSerializer

