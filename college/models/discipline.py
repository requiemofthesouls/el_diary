from django.db import models
from .speciality import Speciality


class Discipline(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'
