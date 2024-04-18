# Generated by Django 4.2.11 on 2024-04-17 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TimeField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.jobstatus', to_field='qualif_level')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_appo', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.stylist', to_field='stylist_id')),
                ('time_appo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointmenttime', to='booking.appointmenttime')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicetype', to='booking.service')),
            ],
        ),
    ]