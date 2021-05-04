from django.core.exceptions import ValidationError
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .forms import CharacterForm, SpendPointsForm
from .models import Character, PotionQuantity
from items.models import Weapon, Armor, Spell, Potion


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

        weapon_equipped = Weapon.objects.filter(character__weapon_equipped_id=self.kwargs['pk'])
        armor_equipped = Armor.objects.filter(character__armor_equipped_id=self.kwargs['pk'])
        Spell.objects.filter(character=self.kwargs['pk'])
        Potion.objects.filter(character=self.kwargs['pk'])

        context['weapon_equipped'] = weapon_equipped
        context['armor_equipped'] = armor_equipped

        return context


class SpendPoints(LoginRequiredMixin, CreateView):
    template_name = 'characters/spend-points.html'
    form_class = SpendPointsForm

    def get_queryset(self):
        return Character.objects.filter(user=self.kwargs['pk'])

    def form_valid(self, form):
        request = self.request
        character = Character.objects.get(user=request.user)
        if request.method == 'POST':
            form = SpendPointsForm(request.POST)
            if form.is_valid():
                strength = form.cleaned_data['strength']
                intelligence = form.cleaned_data['intelligence']
                character.strength += strength
                character.intelligence += intelligence
                character.attribute_points -= strength
                character.attribute_points -= intelligence
                character.save()
                return HttpResponseRedirect(reverse('characters:character-details', args=[character.pk]))

        form = SpendPointsForm
        return render(request, self.template_name, {'form': form})
