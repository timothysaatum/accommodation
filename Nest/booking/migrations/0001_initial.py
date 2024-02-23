# Generated by Django 5.0.1 on 2024-02-22 19:42

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hostel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=30)),
                ('cost', models.FloatField()),
                ('check_in', models.DateField(help_text='YYYY-MM-DD')),
                ('number_of_guests', models.IntegerField()),
                ('phone', models.CharField(max_length=14)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('email_address', models.EmailField(max_length=254)),
                ('uin', models.CharField(max_length=10)),
                ('digital_address', models.CharField(max_length=15)),
                ('receipt', models.CharField(max_length=100)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('is_verified', models.BooleanField(default=False)),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('ref', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.hostel')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.school')),
            ],
        ),
    ]