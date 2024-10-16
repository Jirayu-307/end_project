# Generated by Django 5.1.2 on 2024-10-15 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0001_initial'),
        ('app_rooms', '0002_room_description_alter_room_is_multiple_bed'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='room',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_rooms.room'),
        ),
    ]
