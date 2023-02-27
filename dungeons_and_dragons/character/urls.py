from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('character_list/<slug:char>/', character_list),
]
