# Generated by Django 5.0 on 2024-01-26 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_theater_showtime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='showtime',
            old_name='tname',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='showtime',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showtime', to='home.movie'),
        ),
    ]