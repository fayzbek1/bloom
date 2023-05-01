from django.db import models

# Create your models here.

from django.db import models
from djmoney.models.fields import MoneyField



# Create your models here.

GENDER = [
    ('male','male'),
    ('female','female')
]

SPETSALIST = [
    ('Backend','backend'),
    ('Frontend','frontend'),
    ('Mobile/Android','Mobile/Android'),
    ('Mobile/Ios','Mobile/Ios'),
    
]
ROOM = [
    ('room1','room1'),
    ('room2','room2'),
    ('room3','room3'),
    ('room4','room4'),    
    
]

class Mentor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6,choices=GENDER,default='male')
    birth_date = models.DateField()
    spetsalist = models.CharField(max_length=14,choices=SPETSALIST,default='backend')
    
    def __str__(self):
        return self.first_name + self.last_name
    
    
class Group(models.Model):
    room = models.CharField(max_length=50,choices=ROOM,default='room1')
    create_date = models.DateField()
    mentor = models.OneToOneField(Mentor, on_delete=models.SET_NULL, null=True)   
    subject = models.CharField(max_length=14,choices=SPETSALIST,default='backend') 
    students = models.IntegerField()
    lessons = models.IntegerField()
    price = MoneyField(max_digits=5,decimal_places=2,default_currency='USD') 
    
    def __str__(self):
        return self.room
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6,choices=GENDER,default='male')
    birth_date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)          
    def __str__(self):
        return self.first_name + self.last_name