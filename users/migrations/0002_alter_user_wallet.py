# Generated by Django 3.2.13 on 2024-01-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wallet',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
