# Generated by Django 5.0.1 on 2024-02-11 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_alter_amenities_options_alter_room_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='has_half_payment',
            field=models.BooleanField(default=False),
        ),
    ]