from time import sleep

from arena.services.services import fight
from celery_app import app


@app.task
def random_fight_task():
    from arena.models import Arena
    from characters.models import Character
    from bestiary.models import Bestiary

    fight(Character, Bestiary, Arena)
    fight(Character, Bestiary, Arena)
    fight(Character, Bestiary, Arena)



