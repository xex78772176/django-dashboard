# Generated by Django 3.2.3 on 2021-07-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0002_venue_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue_event',
            name='Date',
            field=models.DateField(),
        ),
    ]
