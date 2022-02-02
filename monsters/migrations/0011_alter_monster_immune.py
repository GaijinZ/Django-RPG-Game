# Generated by Django 3.2 on 2021-04-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0010_alter_monster_immune'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='immune',
            field=models.CharField(choices=[('Fire', 'Fire'), ('Cold', 'Cold')], default='Fire', max_length=50),
        ),
    ]