from django.contrib import admin
from django.contrib.admin import ModelAdmin

from bestiary.models import Bestiary


@admin.register(Bestiary)
class CharacterAdmin(ModelAdmin):
    pass
