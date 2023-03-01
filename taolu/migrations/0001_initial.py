# Generated by Django 4.1.4 on 2023-01-29 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taolu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ПІБ')),
                ('agegroup', models.CharField(max_length=50, verbose_name='Вікова група')),
                ('gender', models.CharField(max_length=50, verbose_name='Стать')),
                ('city_region', models.CharField(max_length=50, verbose_name='Область, місто')),
                ('chanquan', models.CharField(blank=True, max_length=50, verbose_name='Чань цюань')),
                ('nanquan', models.CharField(blank=True, max_length=50, verbose_name='Нань цюань')),
                ('taijiquan', models.CharField(blank=True, max_length=50, verbose_name='Тайцзи цюань')),
                ('daoshu', models.CharField(blank=True, max_length=50, verbose_name='Даошу')),
                ('jianshu', models.CharField(blank=True, max_length=50, verbose_name='Цзянь шу')),
                ('nandao', models.CharField(blank=True, max_length=50, verbose_name='Нань дао')),
                ('taijijian', models.CharField(blank=True, max_length=50, verbose_name='Тайцзицзянь')),
                ('gunshu', models.CharField(blank=True, max_length=50, verbose_name='Гуньшу')),
                ('qianshu', models.CharField(blank=True, max_length=50, verbose_name='Цяншу')),
                ('nangun', models.CharField(blank=True, max_length=50, verbose_name='Нань гунь')),
                ('duilian', models.CharField(blank=True, max_length=50, verbose_name='Дуйлянь')),
                ('trener', models.CharField(max_length=50, verbose_name='Тренер')),
                ('birthday', models.DateTimeField(verbose_name='Дата заповнення')),
            ],
        ),
    ]
