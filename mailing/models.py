from datetime import date

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name='Тема сообщения')
    content = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):
    PERIODS = (
        ("daily", 'Ежедневно'),
        ("weekly", 'Раз в неделю'),
        ("monthly", 'Раз в месяц')
    )
    STATUS_STARTED = 'created'
    STATUS_CREATED = 'started'
    STATUS_DONE = 'done'

    STATUSES = (
        (STATUS_STARTED, 'Запущена'),
        (STATUS_CREATED, 'Создана'),
        (STATUS_DONE, 'Завершена')
    )

    mailing_start_time = models.DateTimeField(verbose_name='Время начала рассылки')
    mailing_stop_time = models.DateTimeField(verbose_name='Время окончания рассылки')
    period = models.CharField(default="daily", max_length=20, choices=PERIODS, verbose_name='Периодичность')
    status = models.CharField(default=STATUS_CREATED, max_length=20, choices=STATUSES, verbose_name='Статус')
    message = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='Сообщение', **NULLABLE)

    def __str__(self):
        return f'С: {self.mailing_start_time} до:  {self.mailing_stop_time} периодичностью в: {self.period}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
