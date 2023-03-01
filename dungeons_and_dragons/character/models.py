from django.db import models
from django.urls import reverse


class CharacterCreate(models.Model):
    DWARF = 'Дварф'
    ELF = 'Эльф'
    HALFLING = 'Полурослик'
    HUMAN = 'Человек'
    DRAGONBORN = 'Драконорожденный'
    GNOME = 'Гном'
    HALF_ELF = 'Полуэльф'
    HALF_ORC = 'Полуорк'
    TIEFLING = 'Тифлинг'

    RACE = [
        (DWARF, 'Дварф'),
        (ELF, 'Эльф'),
        (HALFLING, 'Полурослик'),
        (HUMAN, 'Человек'),
        (DRAGONBORN, 'Драконорожденный'),
        (GNOME, 'Гном'),
        (HALF_ELF, 'Полуэльф'),
        (HALF_ORC, 'Полуорк'),
        (TIEFLING, 'Тифлинг'),

    ]

    LG = 'Законно - добрый'
    NG = 'Нейтрально - добрый'
    CG = 'Хаотично - добрый'
    LN = 'Законно - нейтральный'
    N = 'Нейтральный'
    CN = 'Хаотично - нейтральный'
    LE = 'Законно - злой'
    NE = 'Нейтрально - злой'
    CE = 'Хаотично - злой'

    IDEOLOGY = [
        (LG, 'Законно - добрый'),
        (NG, 'Нейтрально - добрый'),
        (CG, 'Хаотично - добрый'),
        (LN, 'Законно - нейтральный'),
        (N, 'Нейтральный'),
        (CN, 'Хаотично - нейтральный'),
        (LE, 'Законно - злой'),
        (NE, 'Нейтрально - злой'),
        (CE, 'Хаотично - злой'),

        ]

    MALE = 'Мужской'
    FEMALE = 'Женский'

    GENDER = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
        ]

    name = models.CharField('Имя', max_length=20)
    race = models.CharField('Раса', max_length=20, choices=RACE)
    ideology = models.CharField('Мировоззрение', max_length=50, choices=IDEOLOGY)
    description = models.TextField('Описание персонажа', max_length=1000)
    gender = models.CharField('Пол', max_length=20, choices=GENDER)
    portrait = models.ImageField('Портрет', upload_to='portraits/')
    strenght = models.IntegerField('Сила')
    dexterity = models.IntegerField('Ловкость')
    constitution = models.IntegerField('Телосложение')
    intellect = models.IntegerField('Интеллект')
    wizdom = models.IntegerField('Мудрость')
    charisma = models.IntegerField('Харизма')

    DoesNotExist = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Карточка персонажа'
        verbose_name_plural = 'Карточки персонажей'


def get_absolute_url(self):
    return reverse('character', kwargs={'character_id': self.pk})