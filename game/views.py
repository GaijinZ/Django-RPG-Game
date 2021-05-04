import random
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView

from monsters.models import Monster
from characters.models import Character


class HomeView(TemplateView):
    template_name = 'home.html'


class PlayView(LoginRequiredMixin, TemplateView):
    template_name = 'game/play.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        current_player = Character.objects.filter(user=self.kwargs['pk'])
        Monster.create_monster(current_player)
        current_monster = Monster.objects.first()

        context['current_player'] = current_player
        context['current_monster'] = current_monster
        return context


class PlayerAttackMonster(LoginRequiredMixin, TemplateView):
    template_name = 'game/player-attack-monster.html'

    def post(self, request, attack_type=None, *args, **kwargs):
        character = Character.objects.get(user=request.user)
        monster = Monster.objects.first()
        if request.method == 'POST':
            if attack_type == 'weapon':
                weapon_min_dmg = character.weapon_equipped.min_melee_dmg
                weapon_max_dmg = character.weapon_equipped.max_melee_dmg
                dmg = random.randint(weapon_min_dmg, weapon_max_dmg)
                monster.health -= dmg
            if attack_type == 'spell':
                spell = character.spell_equipped.get(id=self.kwargs['pk'])
                if character.current.mana >= spell.mana:
                    if spell.dmg_type != monster.immune:
                        dmg = random.randint(spell.min_spell_dmg, spell.max_spell_dmg)
                        character.current_mana -= spell.mana_cost
                        monster.health -= dmg
                        character.save()
                    else:
                        character.current_mana -= spell.mana_cost
                        character.save()
            if monster.health <= 0:
                character.experience += monster.experience_given
                character.gold += monster.gold_given
                Monster.objects.filter(pk=monster.pk).delete()
                if character.experience >= character.exp_to_lvl_up:
                    character.level += 1
                    character.attribute_points += 2
                    character.exp_to_lvl_up *= 1.5
                character.save()
                return HttpResponseRedirect(reverse('game:play', args=[request.user.pk]))
            monster.save()
            return HttpResponseRedirect(reverse('game:monster-attack-player', args=[request.user.pk]))
        return render(request, self.template_name)


class MonsterAttackPlayer(LoginRequiredMixin, TemplateView):
    template_name = 'game/monster-attack-player.html'

    def post(self, request, *args, **kwargs):
        character = Character.objects.get(user=request.user)
        monster = Monster.objects.first()
        if request.method == 'POST':
            monster_dmg = random.randint(monster.min_dmg, monster.max_dmg)
            character.current_health -= monster_dmg
            if character.current_health <= 0:
                character.experience *= 0.80
                character.current_health = character.max_health
                character.current_mana = character.max_mana
                character.save()
                Monster.objects.filter(pk=monster.pk).delete()
                return HttpResponseRedirect(reverse('game:character-death', args=[request.user.pk]))
            character.save()
            return HttpResponseRedirect(reverse('game:play', args=[request.user.pk]))
        return render(request, self.template_name)


class CharacterDeath(LoginRequiredMixin, TemplateView):
    template_name = 'game/character-death.html'
