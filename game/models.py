from django.db import models
from django.db.models import Q

from characters.models import Character


class PlayerVsPlayer(models.Model):
    creator = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='creator')
    opponent = models.ForeignKey(
        Character, related_name='opponent', on_delete=models.CASCADE, null=True, blank=True)
    completed = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    @staticmethod
    def get_available_games():
        return PlayerVsPlayer.objects.filter(opponent=None, completed=None)

    @staticmethod
    def get_games_for_player(user):
        return PlayerVsPlayer.objects.filter(Q(opponent=user) | Q(creator=user))

    @staticmethod
    def create_new(user):
        new_game = PlayerVsPlayer(creator=user, current_turn=user)
        new_game.save()
        return new_game
