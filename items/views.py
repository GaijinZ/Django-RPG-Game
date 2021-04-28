from django.http import HttpResponseRedirect
from django.db.models import F
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Weapon, Armor, Spell, Potion
from characters.models import Character, PotionQuantity
from .forms import BuyItemForm


class ShopView(LoginRequiredMixin, TemplateView):
    template_name = 'items/shop.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        character = Character.objects.filter(user=self.kwargs['pk'])

        weapons_to_buy = Weapon.objects.exclude(
            name__in=Character.objects.values_list('weapon_equipped__name', flat=True))
        armors_to_buy = Armor.objects.exclude(
            name__in=Character.objects.values_list('armor_equipped__name', flat=True))
        spells_to_buy = Spell.objects.exclude(
            name__in=Character.objects.values_list('spell_equipped__name', flat=True))
        potions_to_buy = Potion.objects.all()

        context['character'] = character
        context['weapons_to_buy'] = weapons_to_buy
        context['armors_to_buy'] = armors_to_buy
        context['spells_to_buy'] = spells_to_buy
        context['potions_to_buy'] = potions_to_buy
        return context


class BuyItems(LoginRequiredMixin, TemplateView):
    template_name = 'items/buy-items.html'

    def post(self, request, item_type=None, *args, **kwargs):
        item = None
        character = Character.objects.get(user=request.user)
        if item_type == 'weapon':
            item = Weapon.objects.get(id=self.kwargs['pk'])
            setattr(character, 'weapon_equipped_id', item.id)
        elif item_type == 'armor':
            item = Armor.objects.get(id=self.kwargs['pk'])
            setattr(character, 'armor_equipped_id', item.id)
        elif item_type == 'spell':
            item = Spell.objects.get(id=self.kwargs['pk'])
            character.spell_equipped.add(item)
        form = BuyItemForm(request.POST)
        if request.method == 'POST':
            if item.price <= character.gold and item.level_required <= character.level:
                character.gold = F('gold') - item.price
                character.save()
                return HttpResponseRedirect(reverse('items:shop'))
            form = BuyItemForm()
        args = {'form': form, 'item': item}
        return render(request, self.template_name, args)


class BuyPotion(LoginRequiredMixin, TemplateView):
    template_name = 'items/buy-potion.html'

    def post(self, request, *args, **kwargs):
        character = Character.objects.get(user=request.user)
        potion = Potion.objects.get(id=self.kwargs['pk'])
        potion_amount = PotionQuantity.objects.filter(potion=potion)
        form = BuyItemForm(request.POST)
        if request.method == 'POST':
            if potion.price <= character.gold:
                character.gold = F('gold') - potion.price
                character.potions_equipped.add(potion)
                for amount in potion_amount:
                    amount.amount += 1
                    amount.save()
                character.save()
                return HttpResponseRedirect(reverse('items:shop'))
            form = BuyItemForm()
        args = {'form': form, 'item': potion}
        return render(request, self.template_name, args)


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


class PotionDetails(LoginRequiredMixin, DetailView):
    model = Potion
    template_name = 'items/potion-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        potion = Potion.objects.filter(potionquantity__potion_id=self.kwargs['pk'])

        potion_details = PotionQuantity.objects.filter(potion__in=potion)

        context['potion_details'] = potion_details
        return context
