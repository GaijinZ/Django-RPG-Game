# Generated by Django 3.2 on 2021-04-29 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0006_auto_20210429_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='immune',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
