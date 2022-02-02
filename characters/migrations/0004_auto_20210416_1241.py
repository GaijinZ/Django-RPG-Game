# Generated by Django 3.2 on 2021-04-16 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_auto_20210415_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='gold',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='max_health',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='character',
            name='max_mana',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.IntegerField(default=1),
        ),
    ]