from django.shortcuts import render
from django.contrib.auth.models import User, Group
from quickstart.models import Project
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, ProjectSerializer


class UserViewSet(viewsets.ModelViewSet):
    pass
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer