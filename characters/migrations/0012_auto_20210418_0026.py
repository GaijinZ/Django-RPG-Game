# Generated by Django 3.2 on 2021-04-17 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_weapon'),
        ('characters', '0011_alter_character_weapon_equipped'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='spell_equipped',
        ),
        migrations.AddField(
            model_name='character',
            name='spell_equipped',
            field=models.ManyToManyField(blank=True, null=True, to='items.Spell'),
        ),
    ]
