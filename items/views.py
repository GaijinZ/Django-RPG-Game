from django.http import HttpResponseRedirect, Http404
from django.db.models import F
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps

from .models import Weapon, Armor, Spell
from characters.models import Character
from .forms import BuyWeaponForm


class ShopView(LoginRequiredMixin, TemplateView):
    template_name = 'items/shop.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        weapons_to_buy = Weapon.objects.exclude(
            name__in=Character.objects.values_list('weapon_equipped__name', flat=True))
        armors_to_buy = Armor.objects.exclude(
            name__in=Character.objects.values_list('armor_equipped__name', flat=True))
        spells_to_buy = Spell.objects.exclude(
            name__in=Character.objects.values_list('spell_equipped__name', flat=True))

        context['weapons_to_buy'] = weapons_to_buy
        context['armors_to_buy'] = armors_to_buy
        context['spells_to_buy'] = spells_to_buy
        return context


class BuyItem(LoginRequiredMixin, TemplateView):
    template_name = 'items/buy-item.html'

    def post(self, request, item_type=None, *args, **kwargs):
        item = None
        if item_type == 'weapon':
            item = Weapon.objects.get(id=self.kwargs['pk'])
        elif item_type == 'armor':
            item = Armor.objects.get(id=self.kwargs['pk'])
        elif item_type == 'spell':
            item = Spell.objects.get(id=self.kwargs['pk'])
        character = Character.objects.get(user=request.user)
        form = BuyWeaponForm(request.POST)
        if request.method == 'POST':
            if item.price <= character.gold:
                character.weapon_equipped_id = item.id
                character.gold = F('gold') - item.price
                character.save()
                return HttpResponseRedirect(reverse('items:shop'))
            form = BuyWeaponForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def get_context_data(self, model=None, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if model == 'weapon':
            model = Weapon.objects.get(id=self.kwargs['pk'])
        elif model == 'armor':
            model = Armor.objects.get(id=self.kwargs['pk'])
        elif model == 'spell':
            model = Spell.objects.get(id=self.kwargs['pk'])

        context['item'] = model
        return context


class WeaponDetails(LoginRequiredMixin, DetailView):
    template_name = 'items/weapon-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        armor_details = Weapon.objects.filter(id=self.kwargs['pk'])

        context['armor_details'] = armor_details
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
