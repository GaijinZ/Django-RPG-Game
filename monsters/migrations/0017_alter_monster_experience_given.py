# Generated by Django 3.2 on 2021-05-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0016_monster_experience_given'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='experience_given',
            field=models.IntegerField(),
        ),
    ]
