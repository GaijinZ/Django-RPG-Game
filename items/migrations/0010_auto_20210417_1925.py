# Generated by Django 3.2 on 2021-04-17 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20210417_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armor',
            name='level_required',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='armor',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='spell',
            name='level_required',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='spell',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='level_required',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='price',
            field=models.IntegerField(),
        ),
    ]
