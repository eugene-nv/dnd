import random

from arena.models import Arena, Log
from characters.services.services import check_level, modifier


def add_characters_in_battle_result(characters_db, enemy_db, battle_db):
    hero = random.choice([i for i in characters_db.objects.all()])
    enemy = random.choice([i for i in enemy_db.objects.all()])

    battle = battle_db.objects.create(hero=hero,
                                      enemy=enemy)

    return battle


def priority(battle_db):
    p = [battle_db.hero, battle_db.enemy]
    random.shuffle(p)
    return [p[0], p[1]]


def attack(battle_instance, attacking, defending):
    attacking_attack = modifier(attacking.strength) + random.randint(1, 20)
    result = defending.ac - attacking_attack
    if attacking.name == battle_instance.hero.name:
        log('Атака', battle_instance, attacking, defending, attacking_attack, result, Log, attacking.level)
    else:
        log('Атака', battle_instance, attacking, defending, attacking_attack, result, Log)
    return result


def damage(battle_instance, attacking, defending):
    attacking_damage = modifier(attacking.strength) + random.randint(1, 6)
    start_hp = defending.hp
    defending.hp -= attacking_damage
    defending.save()

    if defending.hp <= 0:
        battle_instance.result = attacking.name
        battle_instance.save()

        if attacking.name == battle_instance.hero.name:
            attacking.experience += 300
            attacking.level = check_level(attacking)
            attacking.save()

    if attacking.name == battle_instance.hero.name:
        log('Урон', battle_instance, attacking, defending, attacking_damage, defending.hp, Log, start_hp,
            attacking.level)
    else:
        log('Урон', battle_instance, attacking, defending, attacking_damage, defending.hp, Log, start_hp)

    return defending.hp




def log(action, battle, attacking, defending, attacking_attack, defending_hp, log, start_hp=0, start_level=0):
    if action == 'Атака':
        l = log.objects.create(
            battle=battle,
            battle_num=battle.id,
            action=action,
            action_detail=f'Атака {attacking}: {defending.ac} - {attacking_attack} = {defending.ac - attacking_attack}',
            battle_result='1'
        )
        if defending_hp <= 0:
            l.action_result = 'Поподание'
            l.battle_result = '1'
            l.save()
        elif defending_hp > 0:
            l.action_result = 'Промах'
            l.battle_result = '1'
            l.save()

        return l

    if action == 'Урон':
        if defending_hp < 0:
            if attacking.name == battle.hero.name and start_level < attacking.level:
                l = log.objects.create(
                    battle=battle,
                    battle_num=battle.id,
                    action=action,
                    action_detail=f'Урон {attacking}: {start_hp} - {attacking_attack} = {start_hp - attacking_attack}',
                    action_result=f'{attacking} нанес {attacking_attack} урона {defending}',
                    winner=attacking,
                    battle_result=f'{attacking} получил 300 опыта. {attacking} получил новый {attacking.level} уровень.'
                )
            elif attacking.name == battle.hero.name and start_level >= attacking.level:
                l = log.objects.create(
                    battle=battle,
                    battle_num=battle.id,
                    action=action,
                    action_detail=f'Урон {attacking}: {start_hp} - {attacking_attack} = {start_hp - attacking_attack}',
                    action_result=f'{attacking} нанес {attacking_attack} урона {defending}',
                    winner=attacking,
                    battle_result=f'{attacking} получил 300 опыта.'
                )

            else:
                l = log.objects.create(
                    battle=battle,
                    battle_num=battle.id,
                    action=action,
                    action_detail=f'Урон {attacking}: {start_hp} - {attacking_attack} = {start_hp - attacking_attack}',
                    action_result=f'{attacking} нанес {attacking_attack} урона {defending}',
                    winner=attacking,
                    battle_result='1'
                )
        else:
            l = log.objects.create(
                battle=battle,
                battle_num=battle.id,
                action=action,
                action_detail=f'Урон {attacking}: {start_hp} - {attacking_attack} = {start_hp - attacking_attack}',
                action_result=f'{attacking} нанес {attacking_attack} урона {defending}',
                battle_result='1'
            )

        return l


def fight(characters_db, enemy_db, battle_db):
    battle = add_characters_in_battle_result(characters_db, enemy_db, battle_db)

    start_hero_hp = battle.hero.hp
    start_enemy_hp = battle.enemy.hp

    p = priority(battle)

    first = p[0]
    second = p[1]

    while battle.hero.hp >= 0 and battle.enemy.hp >= 0:

        # First character turn

        a1 = attack(battle, first, second)
        if a1 <= 0:
            d1 = damage(battle, first, second)
            battle.save()
            if d1 <= 0:
                break

        # Second character turn

        a2 = attack(battle, second, first)
        if a2 <= 0:
            d2 = damage(battle, second, first)
            battle.save()
            if d2 <= 0:
                break

    battle.hero.hp = start_hero_hp
    battle.hero.save()

    battle.enemy.hp = start_enemy_hp
    battle.enemy.save()

    battle.save()
    return battle.result
