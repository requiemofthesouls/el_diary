from django.db import models
from .people import Human
from .cabinets import Cabinets
# from .group import Group


# TODO: Пофиксить поле группы

class Teacher(Human):
    cabinet = models.ForeignKey(Cabinets, on_delete=models.CASCADE, verbose_name='Кабинет')

    # group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')

    def __str__(self):
        return '%s %s %s' % (self.name, self.surname, self.patronymic)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
