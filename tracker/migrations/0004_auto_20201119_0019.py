# Generated by Django 3.1.3 on 2020-11-19 07:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20201118_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='last_update_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='timer',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
