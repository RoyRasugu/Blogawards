from django.shortcuts import render
from rest_framework import generics, permissions
from blog.models import Project, Profile
from .serializers import ProfileSerializer, ProjectSerializer

# Create your views here.
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    serializer_class = ProfileSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProjectSerializer