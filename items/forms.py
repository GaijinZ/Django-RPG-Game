from django import forms

from .models import Weapon


class BuyWeaponForm(forms.ModelForm):

    class Meta:
        model = Weapon
        widgets = {'name': forms.HiddenInput()}
        exclude = ['min_melee_dmg', 'max_melee_dmg', 'level_required', 'price']
