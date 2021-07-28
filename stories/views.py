from stories.permissions import IsAuthorOrReadOnly
from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import Story
from .serializer import StoriesSerializer

# Create your views here.
class StoriesListView(generics.ListCreateAPIView):    
    serializer_class = StoriesSerializer
    queryset = Story.objects.all()

class StoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoriesSerializer
    queryset = Story.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)