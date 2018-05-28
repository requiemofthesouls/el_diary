from django.db import models


class Human(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')

    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')

    birth_date = models.DateField(verbose_name='Дата рождения')

    class Meta:
        abstract = True




