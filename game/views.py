import random

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView

from monsters.models import Monster
from characters.models import Character
from game.models import PlayerVsPlayer


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

    def spell_attack(self, character, monster):
        spell = character.spell_equipped.get(id=self.kwargs['pk'])
        if character.current_mana >= spell.mana_cost:
            if spell.dmg_type != monster.immune:
                dmg = random.randint(spell.min_spell_dmg, spell.max_spell_dmg)
                character.current_mana -= spell.mana_cost
                monster.health -= dmg
                character.save()
            else:
                character.current_mana -= spell.mana_cost
                character.save()

    def monster_defeat(self, character, monster):
        character.experience += monster.experience_given
        character.gold += monster.gold_given
        Monster.objects.filter(pk=monster.pk).delete()
        if character.experience >= character.exp_to_lvl_up:
            character.level += 1
            character.attribute_points += 2
            character.exp_to_lvl_up *= 1.5
        character.save()

    def post(self, request, attack_type=None, *args, **kwargs):
        character = Character.objects.get(user=request.user)
        monster = Monster.objects.first()
        if request.method == 'POST' and request.is_ajax():
            if monster.health <= 0:
                self.monster_defeat(character, monster)
            weapon_min_dmg = character.weapon_equipped.min_melee_dmg
            weapon_max_dmg = character.weapon_equipped.max_melee_dmg
            dmg = random.randint(weapon_min_dmg, weapon_max_dmg)
            monster.health -= dmg
            monster.save()
            data = {'monster_health': monster.health,
                    'dmg_done': dmg}
            return JsonResponse(data)
        return render(request, self.template_name)


class MonsterAttackPlayer(LoginRequiredMixin, TemplateView):
    template_name = 'game/monster-attack-player.html'

    def player_defeat(self, character, monster):
        character.experience *= 0.80
        character.current_health = character.max_health
        character.current_mana = character.max_mana
        character.save()
        Monster.objects.filter(pk=monster.pk).delete()

    def post(self, request, *args, **kwargs):
        character = Character.objects.get(user=request.user)
        monster = Monster.objects.first()
        if request.method == 'POST':
            monster_dmg = random.randint(monster.min_dmg, monster.max_dmg)
            character.current_health -= monster_dmg
            if character.current_health <= 0:
                self.player_defeat(character, monster)
                return HttpResponseRedirect(reverse('game:character-death', args=[request.user.pk]))
            character.save()
            return HttpResponseRedirect(reverse('game:play', args=[request.user.pk]))
        return render(request, self.template_name)


class LobbyView(TemplateView):
    template_name = 'game/lobby.html'
    model = Character

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # we're creating a list of games that contains just the id (for the link) and the creator
        available_games = [{'creator': game.creator.username, 'id': game.pk} for game in
                           PlayerVsPlayer.get_available_games()]
        # for the player's games, we're returning a list of games with the opponent and id
        player_games = PlayerVsPlayer.get_games_for_player(Character.objects.get(user=self.request.user))

        context['available_games'] = available_games
        context['player_games'] = player_games

        return context


class PlayerVsPlayerView(TemplateView):
    template_name = 'game/player-vs-player.html'


class CharacterDeath(LoginRequiredMixin, TemplateView):
    template_name = 'game/character-death.html'
