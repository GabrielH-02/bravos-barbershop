# Generated by Django 4.2.11 on 2024-04-17 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['date_appo', 'time_appo']},
        ),
        migrations.AlterModelOptions(
            name='appointmenttime',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['title']},
        ),
    ]