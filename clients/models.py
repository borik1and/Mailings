from datetime import date

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Clients(models.Model):
    email = models.EmailField(max_length=150, verbose_name='email')
    name = models.CharField(max_length=50, verbose_name='Имя')
    father_name = models.CharField(max_length=50, verbose_name='Отчество', **NULLABLE)
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    comments = models.CharField(max_length=50, verbose_name='Комментарий', **NULLABLE)
    creation_date = models.DateField(default=date.today, verbose_name='дата создания')
    slug = models.CharField(max_length=200, **NULLABLE, verbose_name='slug')

    def __str__(self):
        return f'Имя: {self.name} email: {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
