from django.views.generic import TemplateView

from .models import Weapon, Armor, Spell
from characters.models import Character


class ShopView(TemplateView):
    template_name = 'items/shop.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        weapon_data = Weapon.objects.filter(name='pk')\
            if Character.objects.filter(weapon_equipped__name='pk').exists()\
            else None
        armor_data = Armor.objects.all()
        spell_data = Spell.objects.all()

        context['weapon_data'] = weapon_data
        context['armor_data'] = armor_data
        context['spell_data'] = spell_data
        return context
