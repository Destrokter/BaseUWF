# Generated by Django 4.1.5 on 2023-02-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tradic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ПІБ')),
                ('birthday', models.DateField(verbose_name='Дата народження')),
                ('rang', models.CharField(blank=True, choices=[('І юн.', 'І юн.'), ('ІІ юн.', 'ІІ юн.'), ('ІІІ юн.', 'ІІІ юн.'), ('І', 'І'), ('ІІ', 'ІІ'), ('ІІІ', 'ІІІ'), ('КМСУ', 'КМСУ'), ('МСУ', 'МСУ'), ('МСМКУ', 'МСМКУ'), ('ЗМСУ', 'ЗМСУ')], default=None, max_length=20, verbose_name='Розряд')),
                ('agegroup', models.CharField(choices=[('до 8р.', 'до 8р.'), ('9-11р.', '9-11р.'), ('12-14р.', '12-14р.'), ('15-17р.', '15-17р.'), ('18+р.', '18+р.')], default=None, max_length=20, verbose_name='Вікова група')),
                ('gender', models.CharField(choices=[('чол', 'чол'), ('жін', 'жін')], default=None, max_length=20, verbose_name='Стать')),
                ('city_region', models.CharField(max_length=50, verbose_name='Область, місто')),
                ('catquan', models.CharField(blank=True, choices=[('ней цзя цюань', 'ней цзя цюань'), ('вай цзя цюань', 'вай цзя цюань'), ('нань цюань', 'нань цюань'), ('тай цзі цюань', 'тай цзі цюань'), ('сян сін цюань', 'сян сін цюань'), ('шао лінь цюань', 'шао лінь цюань'), ('ді тан цюань', 'ді тан цюань'), ('він чун цюань', 'він чун цюань')], default=None, max_length=20, verbose_name='Категорія кулаків')),
                ('catqise', models.CharField(blank=True, choices=[('довга зброя', 'довга зброя'), ('коротка зброя', 'коротка зброя'), ('парна зброя', 'парна зброя'), ('гнучка зброя', 'гнучка зброя')], default=None, max_length=20, verbose_name='Категорія зброї')),
                ('duilian', models.CharField(blank=True, max_length=50, verbose_name='Дуйлянь')),
                ('trener', models.CharField(max_length=50, verbose_name='Тренер')),
            ],
            options={
                'verbose_name': 'Традиційні комплекси',
                'verbose_name_plural': 'Традиційні комплекси',
            },
        ),
    ]
