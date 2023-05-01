from django.urls import path
from .views import *


urlpatterns = []

urlpatterns += [
    path('mentor',MentorList.as_view()),
    path('group',GroupList.as_view()),
    path('student',StudentList.as_view()),
    path('mentorcreate',Mentorcreate.as_view()),
    path('groupcreate',Groupcreate.as_view()),
    path('studentcreate',Studentcreate.as_view()),
    path('mentor/<str:pk>',Mentorall.as_view()),
    path('group/<str:pk>',Groupall.as_view()),
    path('student/<str:pk>',Studentall.as_view()),
    ]
    