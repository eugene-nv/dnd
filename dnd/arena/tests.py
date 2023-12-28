from django.contrib.auth import get_user_model
from django.test import TestCase

from arena.models import Arena, Log
from arena.services.services import add_characters_in_battle_result, priority, attack, damage, log, fight
from bestiary.models import Bestiary
from characters.models import Character

User = get_user_model()


class BattleViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')

        self.character_1 = Character.objects.create(
            race='Полуэльф',
            klass='Плут',

            name='Астарион',
            gender='мужской',
            ideology='Хаотично-доброе',
            portrait='/portrait/Astarion_0.jpeg',

            level=3,
            experience=2600,
            hp=100,
            ac=100,

            strength=30,
            dexterity=30,
            constitution=30,
            intelligence=30,
            wisdom=30,
            charisma=30,

            owner=self.user,
        ),

        self.enemy_1 = Bestiary.objects.create(
            name='Адская гончая',
            kind='Исчадие',
            image='/portrait/Gale_0.jpeg',
            ac=15,
            hp=45,
            strength=17,
            dexterity=12,
            constitution=14,
            intelligence=6,
            wisdom=13,
            charisma=6,
            experience=700,
        )

    def test_add_characters_in_battle_result(self):
        result = add_characters_in_battle_result(Character, Bestiary, Arena)

        party = (h for h in Character.objects.all())
        enemies = (e for e in Bestiary.objects.all())

        self.assertIn(result.hero, party)
        self.assertIn(result.enemy, enemies)

    def test_priority(self):
        battle = add_characters_in_battle_result(Character, Bestiary, Arena)

        p = priority(battle)

        self.assertIn(battle.hero, p)
        self.assertIn(battle.enemy, p)

    def test_attack(self):
        battle = add_characters_in_battle_result(Character, Bestiary, Arena)
        a = attack(battle, battle.hero, battle.enemy)

        self.assertEquals(type(a), int)

        ac = (battle.hero.ac, battle.enemy.ac)
        self.assertIn(100, ac)
        self.assertIn(15, ac)

    def test_damage(self):
        battle = add_characters_in_battle_result(Character, Bestiary, Arena)
        d = damage(battle, battle.hero, battle.enemy)

        self.assertEqual(type(d), int)

    def test_log(self):
        battle = add_characters_in_battle_result(Character, Bestiary, Arena)

        print(f'HP {battle.enemy.hp}')

        self.assertEqual(
            log('Атака', battle, battle.enemy, battle.hero, 8, 92, Log, 45, battle.hero.level).action_result,
            'Промах')

        self.assertEqual(
            log('Урон', battle, battle.enemy, battle.hero, 10, 35, Log, 45, battle.hero.level).action_detail,
            'Урон Адская гончая: 45 - 10 = 35')
        self.assertEqual(
            log('Урон', battle, battle.hero, battle.enemy, 40, 5, Log, 45, battle.hero.level).action_detail,
            'Урон Астарион: 45 - 40 = 5')

        self.assertEqual(
            log('Атака', battle, battle.enemy, battle.hero, 107, -7, Log, 45, battle.hero.level).action_result,
            'Поподание')
        self.assertEqual(
            log('Атака', battle, battle.enemy, battle.hero, 107, -7, Log, 45, battle.hero.level).action,
            'Атака')

    def test_fight(self):
        self.assertEqual(
            fight(Character, Bestiary, Arena), 'Астарион'
        )