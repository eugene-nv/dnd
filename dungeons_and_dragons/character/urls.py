from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('character_list/', character_list, name='character_list'),
    path('character_create/', character_create, name='character_create'),
    path('character/<slug:character_slug>/', character, name='character'),
    path('login/', login, name='login'),
]
