# Generated by Django 3.1.3 on 2020-11-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20201118_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timer',
            name='is_paused',
        ),
        migrations.AddField(
            model_name='timer',
            name='is_running',
            field=models.BooleanField(default=True),
        ),
    ]
