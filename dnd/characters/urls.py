from django.urls import path

from .views import *

urlpatterns = [
    path('', CharacterViews.as_view(), name='home'),
    # path('', index),
    path('characters/', OwnerCharactersViews.as_view(), name='characters'),
    path('characters/<int:pk>/', ShowCharacter.as_view(), name='show_characters'),
    path('characters/<int:pk>/delete/', CharacterDeleteView.as_view(), name='delete_character'),
    path('characters/<int:pk>/update/', CharacterUpdateView.as_view(), name='update_character'),
    path('create/', CreateCharacter.as_view(), name='create'),


]