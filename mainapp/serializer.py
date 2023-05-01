from rest_framework import serializers
from .models import *
#



class MentorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
        
class GroupsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
                

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'                