from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=50)
    max_health = models.IntegerField()
    max_mana = models.IntegerField()
    experience = models.IntegerField()
    level = models.IntegerField()
    gold = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.name
