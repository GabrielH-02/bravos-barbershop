# Generated by Django 4.2.11 on 2024-04-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['-updated_on']},
        ),
        migrations.AlterModelOptions(
            name='hairrequest',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='jobstatus',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='stylist',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='hairrequest',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]