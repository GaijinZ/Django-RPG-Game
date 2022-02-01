from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from items.models import Spell
from .forms import CharacterForm, SpendPointsForm
from .models import Character, PotionQuantity


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
        character_spells = Spell.objects.filter(character__in=character_details)
        character_potions = PotionQuantity.objects.filter(character__in=character_details)

        context['character_details'] = character_details
        context['character_spells'] = character_spells
        context['character_potions'] = character_potions
        return context


class CharacterInventory(LoginRequiredMixin, ListView):
    model = Character
    template_name = 'characters/character-inventory.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        character = Character.objects.get(id=self.kwargs['pk'])
        spells_available = Spell.objects.filter(character__in=character)
        potions_available = PotionQuantity.objects.filter(character__in=character)

        context['character'] = character
        context['spells_available'] = spells_available
        context['potions_available'] = potions_available

        return context


class SpendPoints(LoginRequiredMixin, CreateView):
    template_name = 'characters/spend-points.html'
    form_class = SpendPointsForm

    def get_queryset(self):
        return Character.objects.filter(user=self.kwargs['pk'])

    def form_valid(self, form):
        character = Character.objects.get(user=self.request.user)
        spell_name = Spell.objects.filter(character=character)
        if request.method == 'POST':
            form = SpendPointsForm(self.request.POST)
            if form.is_valid():
                strength = form.cleaned_data['strength']
                intelligence = form.cleaned_data['intelligence']
                character.strength += strength
                character.intelligence += intelligence
                character.max_health += (2 * strength)
                character.max_mana += (2 * intelligence)
                character.weapon_equipped.max_melee_dmg += strength
                for spell in spell_name:
                    spell.max_spell_dmg += intelligence
                character.attribute_points -= strength
                character.attribute_points -= intelligence
                character.current_health = character.max_health
                character.current_mana = character.max_mana
                character.save()
                return HttpResponseRedirect(reverse
                                            ('characters:character-details', args=[character.pk]))

        form = SpendPointsForm
        return render(request, self.template_name, {'form': form})
