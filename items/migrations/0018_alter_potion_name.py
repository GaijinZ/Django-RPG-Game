# Generated by Django 3.2 on 2021-04-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_auto_20210427_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potion',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
