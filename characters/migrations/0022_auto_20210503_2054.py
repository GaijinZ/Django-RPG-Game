# Generated by Django 3.2 on 2021-05-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0021_character_current_mana'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='attribute_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='exp_to_lvl_up',
            field=models.IntegerField(default=1),
        ),
    ]
