# Generated by Django 4.1.5 on 2023-03-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taolu', '0007_taolu_measure'),
    ]

    operations = [
        migrations.AddField(
            model_name='taolu',
            name='note',
            field=models.CharField(default=None, max_length=100, verbose_name='Примітки'),
        ),
    ]