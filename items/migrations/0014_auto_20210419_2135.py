# Generated by Django 3.2 on 2021-04-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0013_auto_20210419_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='dmg_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='spell',
            name='mana_cost',
            field=models.IntegerField(),
        ),
    ]