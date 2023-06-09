from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self , email , username , password = None):
        if username is None:
            raise TypeError('User should have a username')
        if email is None:
            raise TypeError('User should have a email')
        user = self.model(username = username, email = self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email, username,password=None):
        if password is None:
            raise TypeError('User should have a password')
        user = self.create_user(username,email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
    
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def token(self):
        return ''