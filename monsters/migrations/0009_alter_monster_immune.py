# Generated by Django 3.2 on 2021-04-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0008_alter_monster_immune'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='immune',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]