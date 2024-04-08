from django.shortcuts import render, HttpResponse
from django.views import View

# add the restframework components
from rest_framework import generics
from rest_framework.permissions import AllowAny

# import the Donor model and DonorSerializer
from .models import Donor
from .serializers import DonorSerializer
# Create your views here.


class HomeView(View):
    '''
    This is the home view for the API
    '''
    def get(self, request):
        return HttpResponse("Hello, World!")


class DonorList(generics.ListCreateAPIView):
    '''
    This view will return a list of donors or create a new donor record to the database
    '''
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
    permission_classes = [AllowAny]



