import random
from django.db import models


# Create your models here.

class Monster(models.Model):
    IMMUNE_TYPE = (
        ('None', 'None'),
        ('Fire', 'Fire'),
        ('Cold', 'Cold'),
    )

    MONSTER_TYPE = (
        ('Spider', 'Spider'),
        ('Rat', 'Rat'),
        ('Ogre', 'Ogre'),
        ('Troll', 'Troll')
    )

    name = models.CharField(max_length=50)
    health = models.IntegerField()
    min_dmg = models.IntegerField()
    max_dmg = models.IntegerField()
    immune = models.CharField(max_length=50, choices=IMMUNE_TYPE, default=IMMUNE_TYPE[0][0])
    frozen = models.BooleanField(default=False)
    type = models.CharField(max_length=50, choices=MONSTER_TYPE)
    experience_given = models.IntegerField()
    gold_given = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.name

    @classmethod
    def create_monster(cls, current_player):

        SPIDER_ATTRIBUTES = {
            'name': 'Spider',
            'health': random.randint(5, 6),
            'min_dmg': 5,
            'max_dmg': 10,
            'experience_given': random.randint(5, 15),
            'gold_given': random.randint(5, 10),
            'type': 'Spider'
        }

        RAT_ATTRIBUTES = {
            'name': 'Rat',
            'health': random.randint(25, 46),
            'min_dmg': 10,
            'max_dmg': 20,
            'experience_given': random.randint(15, 25),
            'gold_given': random.randint(10, 20),
            'immune': 'Fire',
            'type': 'Rat'
        }

        TROLL_ATTRIBUTES = {
            'name': 'Troll',
            'health': random.randint(45, 66),
            'min_dmg': 25,
            'max_dmg': 35,
            'experience_given': random.randint(25, 35),
            'gold_given': random.randint(20, 35),
            'immune': 'Cold',
            'type': 'Troll'
        }

        OGRE_ATTRIBUTES = {
            'name': 'Ogre',
            'health': random.randint(65, 100),
            'min_dmg': 40,
            'max_dmg': 60,
            'experience_given': random.randint(35, 50),
            'gold_given': random.randint(35, 50),
            'immune': 'Fire',
            'type': 'Ogre'
        }

        old_monster = cls.objects.last()
        # looks rly ugly, if not junior role maybe internship?
        for player in current_player:
            if old_monster is None:
                if player.level < 5:
                    new_monster = cls(**SPIDER_ATTRIBUTES)
                    if old_monster != new_monster:
                        new_monster.save()
                        return new_monster
                    return old_monster
                elif 5 <= player.level < 10:
                    new_monster = cls.objects.create(**RAT_ATTRIBUTES)
                    if old_monster != new_monster:
                        new_monster.save()
                        return new_monster
                    return old_monster
                elif 10 <= player.level < 15:
                    new_monster = cls.objects.create(**TROLL_ATTRIBUTES)
                    if old_monster != new_monster:
                        new_monster.save()
                        return new_monster
                    return old_monster
                elif 15 <= player.level < 30:
                    new_monster = cls.objects.create(**OGRE_ATTRIBUTES)
                    if old_monster != new_monster:
                        new_monster.save()
                        return new_monster
                    return old_monster
            return old_monster
