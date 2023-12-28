from django.db import models

from bestiary.models import Bestiary
from characters.models import Character


class Arena(models.Model):
    hero = models.ForeignKey(to=Character, on_delete=models.CASCADE, related_name='hero', null=True,
                                        blank=True)
    enemy = models.ForeignKey(to=Bestiary, on_delete=models.CASCADE, related_name='enemy', null=True,
                                         blank=True)
    result = models.CharField(max_length=255, verbose_name='Результат', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Арена'
        verbose_name_plural = 'Арена'
        ordering = ['id']

    def __str__(self):
        return f'{self.hero} - {self.enemy}'


class Log(models.Model):
    battle = models.ForeignKey(to=Arena, on_delete=models.CASCADE, related_name='battle', null=True,
                               blank=True)
    battle_num = models.IntegerField(null=True, blank=True)
    action = models.CharField(max_length=255, verbose_name='Действие', blank=True, null=True)
    action_detail = models.CharField(max_length=255, verbose_name='Детализация действия', blank=True, null=True)
    action_result = models.CharField(max_length=255, verbose_name='Результат действия', blank=True, null=True)
    winner = models.CharField(max_length=255, verbose_name='Победитель', blank=True, null=True)
    battle_result = models.CharField(max_length=255, verbose_name='Результат боя', blank=True, null=True)

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Лог'
        ordering = ['id']

    def __str__(self):
        return f'{self.battle}'