from datetime import date
from django.db import models


class Users(models.Model):
    email = models.EmailField(unique=True, max_length=150, verbose_name='email')
    name = models.CharField(max_length=50, verbose_name='Имя')
    father_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True, null=True)
    surname = models.CharField(max_length=50, verbose_name='Фамилия', blank=True, null=True)
    comments = models.CharField(max_length=50, verbose_name='Комментарий', blank=True, null=True)
    creation_date = models.DateField(default=date.today, verbose_name='дата создания')
    password = models.CharField(max_length=20, verbose_name='Ваш пароль', blank=True, null=True)

    def __str__(self):
        return f'Имя: {self.name} email: {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
