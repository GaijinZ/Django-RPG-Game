from django.views.generic import TemplateView

from .models import Weapon, Armor, Spell
from characters.models import Character


class ShopView(TemplateView):
    template_name = 'items/shop.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        weapons_to_buy = Weapon.objects.exclude(name__in=Character.objects.values_list('weapon_equipped__name', flat=True))
        armors_to_buy = Armor.objects.exclude(name__in=Character.objects.values_list('armor_equipped__name', flat=True))
        spells_to_buy = Spell.objects.exclude(name__in=Character.objects.values_list('spell_equipped__name', flat=True))

        context['weapons_to_buy'] = weapons_to_buy
        context['armors_to_buy'] = armors_to_buy
        context['spells_to_buy'] = spells_to_buy
        return context
