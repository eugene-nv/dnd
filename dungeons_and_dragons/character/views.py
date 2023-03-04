from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from character.models import CharacterCreate

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'Список персонажей', 'url_name': 'character_list'},
        {'title': 'Создать персонажа', 'url_name': 'character_create'},
        {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'character/index.html', context)


def character_list(request):
    character = CharacterCreate.objects.all()
    context = {
        'title': 'Список персонажей',
        'character': character
    }
    return render(request, 'character/character_list.html', context)


def character(request, character_slug):
    card = get_object_or_404(CharacterCreate, slug=character_slug)

    context = {
        'card': card,
        'name': card.name
    }
    return render(request, 'character/card.html', context=context)


def character_create(request):
    context = {
        'title': 'Создание персонажа',
    }
    return render(request, 'character/character_create.html', context)


def login(request):
    context = {
        'title': 'Авторизация пользователя',
    }
    return render(request, 'character/login.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сорян =(( Такой страницы не существует =(</h1>')

