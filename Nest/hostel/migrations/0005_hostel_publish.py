# Generated by Django 5.0.1 on 2024-02-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0004_alter_room_occupant_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
