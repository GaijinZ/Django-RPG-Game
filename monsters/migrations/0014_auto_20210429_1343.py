# Generated by Django 3.2 on 2021-04-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0013_alter_monster_immune'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='health',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='monster',
            name='max_dmg',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='monster',
            name='min_dmg',
            field=models.IntegerField(default=1),
        ),
    ]
