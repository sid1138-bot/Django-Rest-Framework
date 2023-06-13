from rest_framework import viewsets
from .models import User, Client, Project
from .serializers import UserSerializer, ClientSerializer, ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    
    serializer_class = ProjectSerializer
