import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from items.models import Spell
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
        create_monster = Monster.create_monster(current_player)
        current_monster = Monster.objects.filter(pk=create_monster.pk)
        spells_available = Spell.objects.filter(character__in=current_player)

        context['current_player'] = current_player
        context['current_monster'] = current_monster
        context['spells_available'] = spells_available
        return context

    def weapon_attack(self, character, monster):
        weapon_min_dmg = character.weapon_equipped.min_melee_dmg
        weapon_max_dmg = character.weapon_equipped.max_melee_dmg
        dmg = random.randint(weapon_min_dmg, weapon_max_dmg)
        monster.health -= dmg

    def spell_attack(self, spell, character, monster):
        if character.current_mana >= spell.mana_cost:
            if spell.dmg_type != monster.immune:
                dmg = random.randint(spell.min_spell_dmg, spell.max_spell_dmg)
                character.current_mana -= spell.mana_cost
                monster.health -= dmg
                character.save()
            else:
                character.current_mana -= spell.mana_cost
                character.save()

    def monster_attack(self, character, monster):
        armor_health = character.armor_equipped.health
        armor_defence = character.armor_equipped.defence
        monster_dmg = random.randint(monster.min_dmg, monster.max_dmg)
        armor_health += character.max_health
        monster_dmg -= armor_defence
        character.current_health -= monster_dmg

    def monster_defeat(self, character, monster):
        character.experience += monster.experience_given
        character.gold += monster.gold_given
        Monster.objects.filter(pk=monster.pk).delete()
        if character.experience >= character.exp_to_lvl_up:
            character.level += 1
            character.attribute_points += 2
            character.exp_to_lvl_up *= 1.5
        character.save()

    def player_defeat(self, character):
        character.experience *= 0.80
        character.current_health = character.max_health
        character.current_mana = character.max_mana
        character.save()

    def post(self, request, *args, **kwargs):
        create_monster = Monster.create_monster(Character.objects.filter(user=self.kwargs['pk']))
        character = Character.objects.get(user=request.user)
        monster = Monster.objects.get_or_create(create_monster)[0]
        spell = character.spell_equipped.get(pk=request.POST.get('id'))
        if request.is_ajax():
            if request.POST.get('action') == 'weapon_id':
                self.weapon_attack(character, monster)
            elif request.POST.get('action') == 'spell_id':
                self.spell_attack(spell, character, monster)
            monster.save()

            if monster.health > 0:
                self.monster_attack(character, monster)
                if character.current_health <= 0:
                    self.player_defeat(character)
                    data = {'status': 0, 'url': '/'}
                    return JsonResponse(data)
                character.save()

            if monster.health <= 0:
                self.monster_defeat(character, monster)

            data = {'status': 1,
                    'monster_id': monster.pk,
                    'monster_health': monster.health,
                    'player_health': character.current_health,
                    'player_mana': character.current_mana,
                    'player_exp': character.experience,
                    'player_lvl': character.level,
                    'monster_type': monster.type}
            return JsonResponse(data)
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
