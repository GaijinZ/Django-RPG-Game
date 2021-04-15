from django.db import models

from characters.models import Character

# Create your models here.


class Shop(models.Model):

    price = models.IntegerField()
    level_required = models.ForeignKey(Character, verbose_name='level required', on_delete=models.CASCADE)

    objects = models.Manager()
