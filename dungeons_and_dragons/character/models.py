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

    BARD = 'Бард'
    BARBARIAN = 'Варвар'
    WARRIOR = 'Воин'
    WIZARD = 'Волшебник'
    DRUID = 'Друид'
    CLERIC = 'Жрец'
    WARLOCK = 'Колдун'
    MONK = 'Монах'
    PALADIN = 'Паладин'
    ROGUE = 'Плут'
    RANGER = 'Следопыт'
    SORCERER = 'Чародей'

    CLASS = [
        (BARD, 'Бард'),
        (BARBARIAN, 'Варвар'),
        (WARRIOR, 'Воин'),
        (WIZARD, 'Волшебник'),
        (DRUID, 'Друид'),
        (CLERIC, 'Жрец'),
        (WARLOCK, 'Колдун'),
        (MONK, 'Монах'),
        (PALADIN, 'Паладин'),
        (ROGUE, 'Плут'),
        (RANGER, 'Следопыт'),
        (SORCERER, 'Чародей'),

    ]

    name = models.CharField(verbose_name='Имя', max_length=255)
    race = models.CharField(verbose_name='Раса', max_length=255, choices=RACE)
    klass = models.CharField(verbose_name='Класс', max_length=255, choices=CLASS)
    ideology = models.CharField(verbose_name='Мировоззрение', max_length=255, choices=IDEOLOGY)
    description = models.TextField(verbose_name='Описание персонажа', max_length=999)
    gender = models.CharField(verbose_name='Пол', max_length=255, choices=GENDER)
    portrait = models.ImageField(verbose_name='Портрет', upload_to='portraits/')
    strenght = models.IntegerField(verbose_name='Сила')
    dexterity = models.IntegerField(verbose_name='Ловкость')
    constitution = models.IntegerField(verbose_name='Телосложение')
    intellect = models.IntegerField(verbose_name='Интеллект')
    wizdom = models.IntegerField(verbose_name='Мудрость')
    charisma = models.IntegerField(verbose_name='Харизма')

    time_create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True, db_index=True)

    DoesNotExist = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Карточка персонажа'
        verbose_name_plural = 'Карточки персонажей'
        ordering = ['time_create']

    def get_absolute_url(self):
        return reverse('character', kwargs={'character_slug': self.slug})