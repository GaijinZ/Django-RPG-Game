from django.db import models


# Create your models here.

class Monster(models.Model):
    name = models.CharField(max_length=50)
    min_health = models.IntegerField()
    max_health = models.IntegerField()
    min_dmg = models.IntegerField()
    max_dmg = models.IntegerField()
    immune = models.CharField(max_length=50)
    frozen = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'
