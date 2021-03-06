# Generated by Django 3.2 on 2021-04-27 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0021_remove_potion_quantity'),
        ('characters', '0016_character_potions_equipped'),
    ]

    operations = [
        migrations.CreateModel(
            name='PotionQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
                ('potion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.potion')),
            ],
            options={
                'unique_together': {('character', 'amount')},
            },
        ),
        migrations.RemoveField(
            model_name='character',
            name='potions_equipped',
        ),
        migrations.AddField(
            model_name='character',
            name='potions_equipped',
            field=models.ManyToManyField(through='characters.PotionQuantity', to='items.Potion'),
        ),
    ]
