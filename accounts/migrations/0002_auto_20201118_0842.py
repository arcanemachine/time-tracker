# Generated by Django 3.1.3 on 2020-11-18 08:42

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeruser',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(blank=True, null=True),
        ),
    ]
