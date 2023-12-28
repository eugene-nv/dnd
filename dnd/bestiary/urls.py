from django.urls import path

from .views import *

urlpatterns = [
    path('', CreaturesViews.as_view(), name='bestiary'),
    path('creatures/<int:pk>/', ShowCreature.as_view(), name='show_creature'),

]