# Generated by Django 3.2.12 on 2022-02-18 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endearapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email_address',
            field=models.EmailField(max_length=60, unique=True, verbose_name='email_address'),
        ),
    ]