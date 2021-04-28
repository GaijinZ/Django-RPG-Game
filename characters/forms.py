from django import forms

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
