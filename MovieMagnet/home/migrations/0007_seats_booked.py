# Generated by Django 5.0 on 2024-01-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_booked_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats_booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('moviename', models.CharField(max_length=255)),
                ('tname', models.CharField(max_length=255)),
            ],
        ),
    ]
