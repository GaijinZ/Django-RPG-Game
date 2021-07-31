from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Weapon, Armor, Spell, Potion
from characters.models import Character, PotionQuantity


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

            if request.POST.get('action') == 'weapon':
                chosen_item = Weapon.objects.get(pk=request.POST.get('id'))
                self.buy_item(character, 'weapon_equipped_id', chosen_item)

            elif request.POST.get('action') == 'armor':
                chosen_item = Armor.objects.get(pk=request.POST.get('id'))
                self.buy_item(character, 'armor_equipped_id', chosen_item)

            elif request.POST.get('action') == 'spell':
                chosen_item = Spell.objects.get(pk=request.POST.get('id'))
                self.buy_spell(character, chosen_item)

            elif request.POST.get('action') == 'potion':
                chosen_item = Potion.objects.get(pk=request.POST.get('id'))
                potion_amount = PotionQuantity.objects.filter(potion=chosen_item)
                if chosen_item.price <= character.gold:
                    character.gold -= chosen_item.price
                    character.potions_equipped.add(chosen_item)
                    for potion in potion_amount:
                        potion.amount += 1
                        potion.save()
                    character.save()

            data = {
                'name': chosen_item.name
            }
            return JsonResponse(data)
        return render(request, self.template_name)
