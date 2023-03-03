from django import template
from character.views import menu

register = template.Library()


@register.simple_tag()
def get_menu():
    return menu


@register.inclusion_tag('character/main_menu.html')
def show_main_menu():
    main_menu = menu
    return {'main_menu': main_menu}
