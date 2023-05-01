from django.urls import path
from .views import *

urlpatterns = [
    path('register/',RegisterApiview.as_view(),name='register'),
]
