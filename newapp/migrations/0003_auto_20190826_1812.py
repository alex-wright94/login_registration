# Generated by Django 2.2.4 on 2019-08-26 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_trip_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='Desc',
            field=models.TextField(max_length=255),
        ),
    ]
