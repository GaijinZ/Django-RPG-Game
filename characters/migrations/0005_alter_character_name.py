# Generated by Django 3.2 on 2021-04-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_auto_20210416_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
