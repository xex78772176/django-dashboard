# Generated by Django 3.2.3 on 2021-07-08 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    
    dependencies = [
        ('iot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Venue', models.CharField(max_length=10)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Timestart', models.TimeField()),
                ('Timeend', models.TimeField()),
                ('Event', models.CharField(max_length=10)),
                ('Instructor', models.CharField(max_length=20)),
                ('temp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hum', models.DecimalField(decimal_places=2, max_digits=5)),
                ('light', models.DecimalField(decimal_places=2, max_digits=5)),
                ('snd', models.DecimalField(decimal_places=2, max_digits=5)),


            ],
        ),
    ]
