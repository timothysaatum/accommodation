# Generated by Django 5.0.1 on 2024-01-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_client_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='id_number',
            field=models.CharField(default=1254789, max_length=50),
            preserve_default=False,
        ),
    ]