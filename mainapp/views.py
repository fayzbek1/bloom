from rest_framework import viewsets,generics,permissions,status
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializer import *
from rest_framework.response import Response

# Create your views here.

class MentorList(generics.ListAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorsSerializers
    
class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializers
    
class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializers    
    
class Mentorcreate(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorsSerializers
    
class Groupcreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializers
    
class Studentcreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializers    
    
class Mentorall(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Mentor.objects.all()
    serializer_class = MentorsSerializers
    
class Groupall(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializers
    
class Studentall(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializers       