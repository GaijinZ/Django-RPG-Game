from django.db import models
from django.urls import reverse


class Character(models.Model):
    name = models.CharField(max_length=50, unique=True)
    max_health = models.IntegerField(default=50)
    max_mana = models.IntegerField(default=30)
    strength = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    level = models.IntegerField(default=1)
    gold = models.IntegerField(default=1)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('characters:character-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
