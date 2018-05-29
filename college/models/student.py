from django.db import models
from .people import Human
from .group import Group


class Student(Human):
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.name, self.surname, self.patronymic, self.group)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
