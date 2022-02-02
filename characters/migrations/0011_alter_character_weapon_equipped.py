# Generated by Django 3.2 on 2021-04-17 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_weapon'),
        ('characters', '0010_character_weapon_equipped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='weapon_equipped',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.weapon'),
        ),
    ]