# Generated by Django 3.2 on 2021-04-17 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_remove_character_weapon_equipped'),
        ('items', '0010_auto_20210417_1925'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Weapon',
        ),
    ]
