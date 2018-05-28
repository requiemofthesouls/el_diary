from django.db import models
from .speciality import Speciality
from .teacher import Teacher


class Group(models.Model):
    GRADE_CHOICES = (
        ('1', '1-ый курс'),
        ('2', '2-ой курс'),
        ('3', '3-ый курс'),
        ('4', '4-ый курс')
    )

    grade = models.CharField(max_length=1, choices=GRADE_CHOICES, verbose_name='Курс')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='Специальность')
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return '%s%s' % (self.grade, self.speciality.number)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
