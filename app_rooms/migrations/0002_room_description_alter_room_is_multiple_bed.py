# Generated by Django 5.1.2 on 2024-10-15 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='is_multiple_bed',
            field=models.BooleanField(default=False),
        ),
    ]
