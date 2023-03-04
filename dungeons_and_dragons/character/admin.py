from django.contrib import admin
from .models import *


class CharacterCreateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'race', 'ideology', 'gender')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'race', 'ideology')
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(CharacterCreate, CharacterCreateAdmin)