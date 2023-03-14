from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from character.models import CharacterCreate
from .forms import AddCharacterForm

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'Список персонажей', 'url_name': 'character_list'},
        {'title': 'Создать персонажа', 'url_name': 'character_create'},
        {'title': 'Войти', 'url_name': 'login'}]


def index(request):

    ''' Главная страница '''

    context = {
        'title': 'Главная страница'
    }
    return render(request, 'character/index.html', context)


@csrf_exempt
def character_list(request):

    ''' Список персонажей '''

    character = CharacterCreate.objects.all()
    context = {
        'title': 'Список персонажей',
        'character': character
    }
    return render(request, 'character/character_list.html', context)


def character(request, character_slug):

    ''' Страница персонажа '''

    card = get_object_or_404(CharacterCreate, slug=character_slug)

    context = {
        'card': card,
        'name': card.name
    }
    return render(request, 'character/card.html', context=context)


def character_create(request):

    ''' Создание персонажа '''

    if request.method == 'POST':
        form = AddCharacterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('character_list')
    else:
        form = AddCharacterForm()
    context = {
        'title': 'Создание персонажа',
        'form': form,
    }
    return render(request, 'character/character_create.html', context)


def login(request):

    ''' Страница авторизации (пока не готова) '''

    context = {
        'title': 'Авторизация пользователя',
    }
    return render(request, 'character/login.html', context)


def pageNotFound(request, exception):

    ''' 404 ошибка '''

    return HttpResponseNotFound('<h1>Сорян =(( Такой страницы не существует =(</h1>')

