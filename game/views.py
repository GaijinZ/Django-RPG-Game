import random

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView

from monsters.models import Monster
from characters.models import Character, PotionQuantity
from items.models import Spell


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
    template_name = 'game/player-attack-monster.html'

    def post(self, request, *args, **kwargs):
        character = Character.objects.get(user=request.user)
        monster = Monster.objects.first()
        if request.method == 'POST':
            character_min_dmg = character.weapon_equipped.min_melee_dmg
            character_max_dmg = character.weapon_equipped.max_melee_dmg
            dmg = random.randint(character_min_dmg, character_max_dmg)
            monster.health -= dmg
            if monster.health <= 0:
                Monster.objects.filter(pk=monster.pk).delete()
                return HttpResponseRedirect(reverse('game:play', args=[request.user.pk]))
            monster.save()
            return HttpResponseRedirect(reverse('game:monster-attack-player', args=[request.user.pk]))
        return render(request, self.template_name)


class MonsterAttackPlayer(TemplateView):
    template_name = 'game/monster-attack-player.html'

    def post(self, request, *args, **kwargs):
        character = Character.objects.get(user=request.user)
        monster = Monster.objects.first()
        if request.method == 'POST':
            monster_dmg = random.randint(monster.min_dmg, monster.max_dmg)
            character.current_health -= monster_dmg
            if character.current_health <= 0:
                character.current_health = character.max_health
                character.save()
                Monster.objects.filter(pk=monster.pk).delete()
                return HttpResponseRedirect(reverse('game:character-death', args=[request.user.pk]))
            character.save()
            return HttpResponseRedirect(reverse('game:play', args=[request.user.pk]))
        return render(request, self.template_name)


class CharacterDeath(TemplateView):
    template_name = 'game/character-death.html'
