# Generated by Django 3.2 on 2021-05-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0018_monster_gold_given'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='gold_given',
            field=models.IntegerField(),
        ),
    ]
