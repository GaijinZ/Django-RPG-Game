from django.db import models
from django.urls import reverse

from accounts.models import Account
from items.models import Weapon, Armor, Spell


class Character(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    max_health = models.IntegerField(default=50)
    max_mana = models.IntegerField(default=20)
    strength = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    level = models.IntegerField(default=1)
    gold = models.IntegerField(default=1)
    weapon_equipped = models.ForeignKey(Weapon, on_delete=models.CASCADE, default=1)
    armor_equipped = models.ForeignKey(Armor, on_delete=models.CASCADE, default=1)
    spell_equipped = models.ManyToManyField(Spell, default=1)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('characters:character-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
