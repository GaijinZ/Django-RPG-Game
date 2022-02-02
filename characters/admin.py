from django.contrib import admin
from .models import Character, PotionQuantity, CharacterToPlay


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Character)
admin.site.register(PotionQuantity)
admin.site.register(CharacterToPlay)
