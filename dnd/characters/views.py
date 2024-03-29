import random

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from datetime import datetime
from .forms import CharacterForm
from .models import Character
from .services.services import modifier, dice_hp


def index(request):
    return render(request, 'index.html')


class CharacterViews(ListView):
    template_name = 'character/home.html'
    model = Character
    context_object_name = 'characters'


class OwnerCharactersViews(ListView):
    template_name = 'character/user_character.html'
    context_object_name = 'characters'

    def get_queryset(self):
        return Character.objects.filter(owner=self.request.user)


class CreateCharacter(CreateView):
    form_class = CharacterForm
    template_name = 'character/create.html'
    success_url = reverse_lazy('home')

    model = Character

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.level = 1
        instance.experience = 0
        instance.hp = modifier(instance.constitution) + random.randint(1, dice_hp(instance.klass))
        instance.ac = modifier(instance.dexterity) + modifier(instance.constitution) + 10
        instance.save()
        return super().form_valid(form)


class ShowCharacter(DetailView):
    model = Character
    template_name = 'character/character_card.html'
    context_object_name = 'char'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class CharacterDeleteView(DeleteView):
    model = Character
    success_url = reverse_lazy("home")
    context_object_name = 'char'
    template_name = 'character/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class CharacterUpdateView(UpdateView):
    model = Character
    fields = ['name', 'portrait', 'ideology']
    template_name = 'character/update.html'
    success_url = reverse_lazy("characters")
    extra_context = {'time': str(datetime.now().time()).split(':')[0]}



