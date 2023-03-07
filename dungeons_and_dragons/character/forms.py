from django import forms
from .models import *


class AddCharacterForm(forms.ModelForm):
    class Meta:
        model = CharacterCreate
        fields = ['name', 'race', 'klass', 'ideology', 'description', 'gender', 'portrait',
                  'strenght', 'dexterity', 'constitution', 'intellect', 'wizdom', 'charisma', 'slug']