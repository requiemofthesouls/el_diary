from django.db import models
from .people import Human
from .group import Group


class Student(Human):
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
