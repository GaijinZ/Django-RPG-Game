from django import forms
from django.db.models import Sum

from .models import Character


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.request.user
        obj.save()
        return obj

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Character.objects.filter(name__iexact=name):
            raise forms.ValidationError("Name already exists.")
        return name


class SpendPointsForm(forms.ModelForm):
    disabled_fields = ('attribute_points',)

    class Meta:
        model = Character
        fields = ('attribute_points', 'strength', 'intelligence',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attribute_points = Character.objects.values_list('attribute_points', flat=True).get()
        self.fields['attribute_points'].initial = attribute_points
        for field in self.disabled_fields:
            self.fields[field].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        strength = cleaned_data.get('strength')
        intelligence = cleaned_data.get('intelligence')
        attribute_points = Character.objects.values_list('attribute_points', flat=True).get()
        sum_of_fields = strength + intelligence
        if sum_of_fields > attribute_points:
            raise forms.ValidationError('Not enough points')
        return cleaned_data
