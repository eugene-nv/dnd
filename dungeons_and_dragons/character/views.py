from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from character.models import CharacterCreate

menu = ['Главная страница', 'Список персонажей', 'Создать персонажа', 'Войти']


def index(request):
    return render(request, 'character/index.html', {'menu': menu, 'title': 'Главная страница'})


def character_list(request):
    character = CharacterCreate.objects.all()
    return render(request, 'character/character_list.html', {'menu': menu, 'title': 'Список персонажей', 'character': character})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сорян =(( Такой страницы не существует =(</h1>')