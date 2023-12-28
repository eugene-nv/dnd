from django.db import models


class Bestiary(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    kind = models.CharField(max_length=255, verbose_name='Вид')
    image = models.ImageField(upload_to='bestiary/images/', null=True, verbose_name='Изображение')

    ac = models.IntegerField(verbose_name='Класс брони')
    hp = models.IntegerField(verbose_name='Очки здоровья')

    strength = models.IntegerField(verbose_name='Сила')
    dexterity = models.IntegerField(verbose_name='Ловкость')
    constitution = models.IntegerField(verbose_name='Телосложение')
    intelligence = models.IntegerField(verbose_name='Интеллект')
    wisdom = models.IntegerField(verbose_name='Мудрость')
    charisma = models.IntegerField(verbose_name='Харизма')

    experience = models.IntegerField(verbose_name='Опыт')

    class Meta:
        verbose_name = 'Бестиарий'
        verbose_name_plural = 'Бестиарий'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'
