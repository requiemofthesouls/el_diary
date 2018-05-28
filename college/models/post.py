from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    date = models.DateField(verbose_name='Дата создания', default=timezone.now)
    content = models.TextField(blank=True, verbose_name='Содержание новости')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
