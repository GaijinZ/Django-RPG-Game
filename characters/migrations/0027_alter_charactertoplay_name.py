# Generated by Django 3.2 on 2022-02-02 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0026_auto_20220202_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactertoplay',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.character'),
        ),
    ]