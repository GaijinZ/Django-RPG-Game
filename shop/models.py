from django.db import models

from items.models import Item
from characters.models import Character

# Create your models here.


class Shop(models.Model):
    item_name = models.ForeignKey(Item, related_name='item_name', on_delete=models.CASCADE)
    price = models.IntegerField()
    level_required = models.ForeignKey(Character, on_delete=models.CASCADE)

    objects = models.Manager()
