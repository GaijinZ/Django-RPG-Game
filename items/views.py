from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Weapon, Armor, Spell
from characters.models import Character


class ShopView(LoginRequiredMixin, TemplateView):
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


class WeaponDetails(LoginRequiredMixin, DetailView):
    model = Weapon
    template_name = 'items/weapon-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        weapon_details = Weapon.objects.filter(id=self.kwargs['pk'])

        context['weapon_details'] = weapon_details
        return context


class ArmorDetails(LoginRequiredMixin, DetailView):
    model = Armor
    template_name = 'items/armor-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        armor_details = Armor.objects.filter(id=self.kwargs['pk'])

        context['armor_details'] = armor_details
        return context


class SpellDetails(LoginRequiredMixin, DetailView):
    model = Spell
    template_name = 'items/spell-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        spell_details = Spell.objects.filter(id=self.kwargs['pk'])

        context['spell_details'] = spell_details
        return context
