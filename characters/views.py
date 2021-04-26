from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CharacterForm
from .models import Character
from items.models import Weapon, Armor, Spell


class CharacterCreationView(LoginRequiredMixin, CreateView):
    form_class = CharacterForm
    template_name = 'characters/character-creation.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class CharacterListView(LoginRequiredMixin, ListView):
    model = Character
    template_name = 'characters/character-list.html'

    def get_queryset(self):
        return Character.objects.filter(user=self.kwargs['pk'])


class CharacterDetailsView(LoginRequiredMixin, DetailView):
    model = Character
    template_name = 'characters/character-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        character_details = Character.objects.filter(id=self.kwargs['pk'])

        context['character_details'] = character_details
        return context


class CharacterInventory(LoginRequiredMixin, ListView):
    model = Character
    template_name = 'characters/character-inventory.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        weapon_equipped = Weapon.objects.filter(
            name__in=Character.objects.values_list('weapon_equipped__name', flat=True))
        armor_equipped = Armor.objects.filter(
            name__in=Character.objects.values_list('armor_equipped__name', flat=True))
        spell_equipped = Spell.objects.filter(
            name__in=Character.objects.values_list('spell_equipped__name', flat=True))

        context['weapon_equipped'] = weapon_equipped
        context['armor_equipped'] = armor_equipped
        context['spell_equipped'] = spell_equipped
        return context
