# Generated by Django 4.1.5 on 2023-03-09 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allbase', '0003_alter_allbase_part'),
        ('taolu', '0009_alter_taolu_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taolu',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='allbase.allbase', verbose_name='ПІБ'),
        ),
    ]
