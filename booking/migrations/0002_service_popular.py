# Generated by Django 4.2.11 on 2024-04-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='popular',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
