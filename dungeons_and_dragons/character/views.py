from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from character.models import CharacterCreate

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'Список персонажей', 'url_name': 'character_list'},
        {'title': 'Создать персонажа', 'url_name': 'character_create'},
        {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'character/index.html', context)


def character_list(request):
    character = CharacterCreate.objects.all()
    context = {
        'menu': menu,
        'title': 'Список персонажей',
        'character': character
    }
    return render(request, 'character/character_list.html', context)


def character(request, character_id): # После добавления персонажей в базу данных и оформления шаблона нужно прописать url <a href="{{ char.get_absolute_url }}"
    return HttpResponse(f'Персонаж с id = {character_id}')

def character_create(request):
    return HttpResponse('Создание персонажа')


def login(request):
    return HttpResponse('Войти в личный кабинет')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сорян =(( Такой страницы не существует =(</h1>')

