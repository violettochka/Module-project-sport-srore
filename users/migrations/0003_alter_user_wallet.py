# Generated by Django 3.2.13 on 2024-01-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wallet',
            field=models.IntegerField(blank=True, default=10000, null=True),
        ),
    ]
