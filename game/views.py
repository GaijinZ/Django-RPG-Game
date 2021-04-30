import random

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView

from monsters.models import Monster
from characters.models import Character, PotionQuantity
from items.models import Spell
from .forms import AttackMonsterForm


class HomeView(TemplateView):
    template_name = 'home.html'


class PlayView(TemplateView):
    template_name = 'game/play.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        current_player = Character.objects.filter(user=self.kwargs['pk'])
        character_spells = Spell.objects.filter(character__in=current_player)
        character_potions = PotionQuantity.objects.filter(character__in=current_player)

        Monster.create_monster(current_player)

        current_monster = Monster.objects.first()

        context['current_player'] = current_player
        context['character_spells'] = character_spells
        context['character_potions'] = character_potions
        context['current_monster'] = current_monster
        return context


class PlayerAttackMonster(TemplateView):
    template_name = 'game/attack-monster.html'

    def post(self, request, *args, **kwargs):
        character = Character.objects.get(user=request.user)
        monster = Monster.objects.first()
        if request.method == 'POST':
            min_dmg = character.weapon_equipped.min_melee_dmg
            max_dmg = character.weapon_equipped.max_melee_dmg
            dmg = random.randint(min_dmg, max_dmg + 1)
            monster.health -= dmg
            monster.save()
            return HttpResponseRedirect(reverse('game:play', args=[request.user.pk]))
        return render(request, self.template_name)
