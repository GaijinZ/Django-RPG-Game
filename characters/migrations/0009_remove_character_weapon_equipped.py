# Generated by Django 3.2 on 2021-04-17 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_auto_20210417_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='weapon_equipped',
        ),
    ]
