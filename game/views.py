from django.shortcuts import render
from django.views.generic import TemplateView

from monsters.models import Monster


class HomeView(TemplateView):
    template_name = 'home.html'


class PlayView(TemplateView):
    template_name = 'game/play.html'

