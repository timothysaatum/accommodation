# Generated by Django 5.0.1 on 2024-01-31 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_client_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]