# Generated by Django 3.2.5 on 2021-07-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animal_type',
            field=models.CharField(max_length=30),
        ),
    ]