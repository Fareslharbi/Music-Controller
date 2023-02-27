from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Room
from .serializers import RoomSerializer
# Create your views here.

# class UserViewSet(ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer