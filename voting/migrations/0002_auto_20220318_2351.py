# Generated by Django 3.1.1 on 2022-03-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
