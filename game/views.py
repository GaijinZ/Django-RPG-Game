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
        current_monster = Monster.objects.first()

        Monster.create_monster(current_player)

        context['current_player'] = current_player
        context['character_spells'] = character_spells
        context['character_potions'] = character_potions
        context['current_monster'] = current_monster
        return context
