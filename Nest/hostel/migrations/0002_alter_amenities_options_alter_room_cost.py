# Generated by Django 5.0.1 on 2024-02-11 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenities',
            options={'verbose_name_plural': 'Amenities'},
        ),
        migrations.AlterField(
            model_name='room',
            name='cost',
            field=models.FloatField(),
        ),
    ]