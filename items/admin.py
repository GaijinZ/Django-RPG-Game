from django.contrib import admin
from .models import Weapon, Armor, Spell, Potion
# Register your models here.
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Spell)
admin.site.register(Potion)
