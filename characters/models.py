from django.db import models
from django.urls import reverse

from accounts.models import Account
from items.models import Weapon, Armor, Spell, Potion


class Character(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    max_health = models.IntegerField(default=50)
    current_health = models.IntegerField(default=50)
    max_mana = models.IntegerField(default=20)
    current_mana = models.IntegerField(default=20)
    exp_to_lvl_up = models.IntegerField(default=50)
    attribute_points = models.IntegerField(default=0)
    strength = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    level = models.IntegerField(default=1)
    gold = models.IntegerField(default=1)
    weapon_equipped = models.ForeignKey(Weapon, on_delete=models.CASCADE, default=1)
    armor_equipped = models.ForeignKey(Armor, on_delete=models.CASCADE, default=1)
    spell_equipped = models.ManyToManyField(Spell, default=1)
    potions_equipped = models.ManyToManyField(Potion, through='PotionQuantity')

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('characters:character-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class PotionQuantity(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    potion = models.ForeignKey(Potion, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    objects = models.Manager()

    def __str__(self):
        return str(self.character)

    class Meta:
        unique_together = [['character', 'potion']]
