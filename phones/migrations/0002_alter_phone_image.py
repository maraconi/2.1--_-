# Generated by Django 3.2.9 on 2021-11-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(),
        ),
    ]
