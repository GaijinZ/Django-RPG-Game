from django.db import models


# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50)
    min_melee_dmg = models.IntegerField()
    max_melee_dmg = models.IntegerField()
    min_ranged_dmg = models.IntegerField()
    max_ranged_dmg = models.IntegerField()
    defence = models.IntegerField()
    health = models.IntegerField()

    objects = models.Manager()
