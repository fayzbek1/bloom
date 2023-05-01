from rest_framework import serializers
from .models import *

class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50,min_length = 8, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        
        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphamueric character')
        
        return attrs
    
    def create(self, validated_data):
        return User.object.create_user(**validated_data)