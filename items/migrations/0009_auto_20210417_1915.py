# Generated by Django 3.2 on 2021-04-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20210417_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='armor',
            name='level_required',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='armor',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='spell',
            name='level_required',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='spell',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]