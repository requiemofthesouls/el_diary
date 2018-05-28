from django.db import models


class Speciality(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='Номер')
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return '%s %s' % (self.number, self.title)

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
