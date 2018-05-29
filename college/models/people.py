from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('M', 'Мужской'),
    ('F', 'Женский'),
)


class Human(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    birth_date = models.DateField(verbose_name='Дата рождения')

    class Meta:
        abstract = True


class UserProfile(models.Model):
    # user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    pass
