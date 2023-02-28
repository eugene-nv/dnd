from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('character_list/', character_list, name='character_list'),
]
