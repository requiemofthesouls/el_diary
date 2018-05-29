from django import forms
from django.contrib.auth.models import User
from college.models import Teacher, Cabinets
from college.models.people import GENDER_CHOICES

YEARS = [x for x in range(1940, 2021)]


# TODO: Сделать валидацию данных
class AddTeacherForm(forms.ModelForm):
    surname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-4',
            'placeholder': 'Иванов'
        }
    ),
        help_text='Фамилия:')

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-4',
            'placeholder': 'Иван'
        }
    ),
        help_text='Имя:')

    patronymic = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-4',
            'placeholder': 'Иванович'
        }
    ),
        help_text='Отчество:')

    gender = forms.ChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-control mb-4',
            'placeholder': 'Мужской'
        }
    ),
        help_text='Пол:',
        choices=GENDER_CHOICES)

    birth_date = forms.DateField(widget=forms.SelectDateWidget(
        years=YEARS,
        attrs={
            'class': 'form-group form-control mb-4'
        }),
        help_text='Дата рождения')

    cabinet = forms.ModelChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-control mb-4'
        }),
        queryset=Cabinets.objects.all(),
        help_text='Выберите кабинет')

    class Meta:
        model = Teacher
        fields = ('surname',)
