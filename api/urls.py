from django.urls import path
from .views import *
from .views import DonorList

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('donors/', DonorList.as_view(), name='donor-list'),
    ]
