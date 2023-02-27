from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse('Главная страница сайта')


def character_list(request, char):
    return HttpResponse(f'<h1>Список созданных персонажей</h1><p>{char}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сорян =(( Такой страницы не существует =(</h1>')