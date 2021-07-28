from django.http import HttpResponseRedirect
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, ListView
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

    def buy_item(self, character, item_type, chosen_weapon):
        if chosen_weapon.price and chosen_weapon.level_required <= character.gold and character.level:
            setattr(character, item_type, chosen_weapon)
            character.gold -= chosen_weapon.price
            character.save()

    def buy_spell(self, character, chosen_spell):
        if chosen_spell.price and chosen_spell.level_required <= character.gold and character.level:
            character.spell_equipped.add(chosen_spell)
            character.save()

    def post(self, request, *args, **kwargs):
        chosen_item = None
        character = Character.objects.get(user=request.user)
        if request.is_ajax():
            if request.POST.get('action') == 'weapon_pk':
                chosen_item = Weapon.objects.get(pk=request.POST.get('id'))
                self.buy_item(character, 'weapon_equipped_id', chosen_item)
            elif request.POST.get('action') == 'armor_pk':
                chosen_item = Armor.objects.get(pk=request.POST.get('id'))
                self.buy_item(character, 'armor_equipped_id', chosen_item)
            elif request.POST.get('action') == 'spell_pk':
                chosen_item = Spell.objects.get(pk=request.POST.get('id'))
                self.buy_spell(character, chosen_item)

            data = {
                'name': chosen_item.name
            }
            return JsonResponse(data)
        return render(request, self.template_name)


class BuyPotion(LoginRequiredMixin, TemplateView):
    template_name = 'items/buy-potion.html'

    def post(self, request, *args, **kwargs):
        character = Character.objects.get(user=request.user)
        chosen_potion = Potion.objects.get(id=self.kwargs['pk'])
        potion_amount = PotionQuantity.objects.filter(potion=chosen_potion)
        form = BuyItemForm(request.POST)
        if request.method == 'POST':
            if chosen_potion.price <= character.gold:
                character.gold = F('gold') - chosen_potion.price
                character.potions_equipped.add(chosen_potion)
                for potion in potion_amount:
                    potion.amount += 1
                    potion.save()
                character.save()
                return HttpResponseRedirect(reverse('items:shop'))
            form = BuyItemForm()
        args = {'form': form, 'item': chosen_potion}
        return render(request, self.template_name, args)


class SpellsAvailable(LoginRequiredMixin, ListView):
    template_name = 'items/spells-available.html'
    model = Spell

    def get_queryset(self):
        return Spell.objects.filter(character=self.kwargs['pk'])


class PotionsAvailable(LoginRequiredMixin, ListView):
    template_name = 'items/potions-available.html'
    model = Potion

    def get_queryset(self):
        return Potion.objects.filter(character=self.kwargs['pk'])


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


class UsePotion(LoginRequiredMixin, TemplateView):
    template_name = 'items/use-potion.html'

    def post(self, request, potion_type=None, *args, **kwargs):
        potion = Potion.objects.filter(id=self.kwargs['pk'])
        character = Character.objects.get(user=request.user)
        current_potions = PotionQuantity.objects.get(potion__in=potion)
        if request.method == 'POST':
            if potion_type == 'Health Potion':
                character.current_health = character.max_health
                character.save()
                current_potions.amount -= 1
                current_potions.save()
                return HttpResponseRedirect(reverse('game:play', args=[request.user.pk]))
            if potion_type == 'Mana Potion':
                character.current_mana = character.max_mana
                character.save()
                current_potions.amount -= 1
                current_potions.save()
                return HttpResponseRedirect(reverse('game:play', args=[request.user.pk]))
        return render(request, self.template_name)
