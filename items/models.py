from django.db import models


class Weapon(models.Model):
    name = models.CharField(max_length=50)
    min_melee_dmg = models.IntegerField()
    max_melee_dmg = models.IntegerField()
    level_required = models.IntegerField()
    price = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.name


class Spell(models.Model):
    name = models.CharField(max_length=50)
    min_spell_dmg = models.IntegerField()
    max_spell_dmg = models.IntegerField()
    level_required = models.IntegerField()
    price = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.name


class Armor(models.Model):
    name = models.CharField(max_length=50)
    defence = models.IntegerField()
    health = models.IntegerField()
    level_required = models.IntegerField()
    price = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.name


class Potion(models.Model):
    pass
