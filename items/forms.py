from django import forms


class BuyItemForm(forms.Form):
    name = forms.CharField()
