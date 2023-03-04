from django.db import models
from datetime import datetime

class Taolu(models.Model):

    AGEGROUP_CHOICES = [
        ('до 8р.', 'до 8р.'),
        ('9-11р.', '9-11р.'),
        ('12-14р.', '12-14р.'),
        ('15-17р.', '15-17р.'),
        ('18+р.', '18+р.'),
     ]
    GENDER_CHOICES = [
        ('чол', 'чол'),
        ('жін', 'жін'),
    ]
    CATQUAN_CHOICES = [
        ('чань цюань', 'чань цюань'),
        ('нань цюань', 'нань цюань'),
        ('тайцзи цюань', 'тайцзи цюань'),
    ]
    CATDUANQISE_CHOICES = [
        ('даошу', 'даошу'),
        ('цзяньшу', 'цзяньшу'),
        ('нань дао', 'нань дао'),
        ('тайцзи цзянь', 'тайцзи цзянь'),
    ]
    CATCHANQISE_CHOICES = [
        ('гунь шу', 'гуньшу'),
        ('цян шу', 'цяншу'),
        ('нань гунь', 'нань гунь'),
    ]
    RANG_CHOICES = [
        ('І юн.', 'І юн.'),
        ('ІІ юн.', 'ІІ юн.'),
        ('ІІІ юн.', 'ІІІ юн.'),
        ('І', 'І'),
        ('ІІ', 'ІІ'),
        ('ІІІ', 'ІІІ'),
        ('КМСУ', 'КМСУ'),
        ('МСУ', 'МСУ'),
        ('МСМКУ', 'МСМКУ'),
        ('ЗМСУ', 'ЗМСУ'),
    ]
    
    measure = models.CharField('Назва заходу', max_length=100, default=None)
    name = models.CharField('ПІБ', max_length=50)
    birthday = models.DateField('Дата народження')
    rang = models.CharField('Розряд',max_length=20, choices=RANG_CHOICES, default=None, blank=True)
    agegroup = models.CharField('Вікова група',max_length=20, choices=AGEGROUP_CHOICES, default=None)
    gender = models.CharField('Стать',max_length=20, choices=GENDER_CHOICES, default=None )
    city_region = models.CharField('Область, місто',max_length=50)
    catquan = models.CharField('Категорія кулаків',max_length=20, choices=CATQUAN_CHOICES, default=None, blank=True)
    catduanqise = models.CharField('Категорія короткої зброї', max_length=20, choices=CATDUANQISE_CHOICES, default=None, blank=True)
    catchanqise = models.CharField('Категорія довгої зброї', max_length=20, choices=CATCHANQISE_CHOICES, default=None, blank=True)
    # chanquan = models.CharField('Чань цюань',max_length=50, blank=True)
    # nanquan = models.CharField('Нань цюань',max_length=50, blank=True)
    # taijiquan = models.CharField('Тайцзи цюань',max_length=50, blank=True)
    # daoshu = models.CharField('Даошу',max_length=50, blank=True)
    # jianshu = models.CharField('Цзянь шу',max_length=50, blank=True)
    # nandao = models.CharField('Нань дао',max_length=50, blank=True)
    # taijijian = models.CharField('Тайцзицзянь',max_length=50, blank=True)
    # gunshu = models.CharField('Гуньшу',max_length=50, blank=True)
    # qianshu = models.CharField('Цяншу',max_length=50, blank=True)
    # nangun = models.CharField('Нань гунь',max_length=50, blank=True)
    duilian = models.CharField('Дуйлянь',max_length=50, blank=True)
    trener = models.CharField('Тренер',max_length=50)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/taolu/{self.id}'

    class Meta:
        verbose_name = 'Таолу'
        verbose_name_plural = 'Таолу'