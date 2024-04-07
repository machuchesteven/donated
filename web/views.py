from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.


class HomeView(View):
    '''
    This is the home view for the API
    '''

    def get(self, request):
        return HttpResponse("Hello, World! from web")