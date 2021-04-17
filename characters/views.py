from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CharacterForm
from .models import Character


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

        character_data = Character.objects.filter(id=self.kwargs['pk'])

        context['character_data'] = character_data
        return context


class CharacterInventory(ListView):
    pass
