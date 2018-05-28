from django.db import models


class Cabinets(models.Model):
    num = models.PositiveSmallIntegerField(verbose_name='Номер')

    def __str__(self):
        return str(self.num)

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'
