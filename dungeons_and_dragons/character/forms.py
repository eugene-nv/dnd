from django import forms
from .models import *


class AddCharacterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['race'].empty_label = 'Выберете расу'
        self.fields['klass'].empty_label = 'Выберете класс'
        self.fields['ideology'].empty_label = 'Выберете мировоззрение'
        self.fields['gender'].empty_label = 'Выберете пол'


    class Meta:
        model = CharacterCreate
        fields = ['name', 'race', 'klass', 'ideology', 'description', 'gender', 'portrait',
                  'strenght', 'dexterity', 'constitution', 'intellect', 'wizdom', 'charisma', 'slug']