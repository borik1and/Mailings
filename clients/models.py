from datetime import date
from django.db import models
from users.models import Users


class Clients(models.Model):
    email = models.EmailField(max_length=150, verbose_name='email')
    name = models.CharField(max_length=50, verbose_name='Имя')
    father_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True, null=True)
    surname = models.CharField(max_length=50, verbose_name='Фамилия', blank=True, null=True)
    comments = models.CharField(max_length=50, verbose_name='Комментарий', blank=True, null=True)
    creation_date = models.DateField(default=date.today, verbose_name='дата создания')
    slug = models.CharField(max_length=200, blank=True, null=True, verbose_name='slug')

    def __str__(self):
        return f'Имя: {self.name} email: {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
