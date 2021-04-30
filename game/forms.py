from django import forms


class AttackMonsterForm(forms.Form):
    name = forms.CharField()
