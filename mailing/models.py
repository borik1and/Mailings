from django.db import models
from django.utils.datetime_safe import datetime

NULLABLE = {'blank': True, 'null': True}


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

    subject = models.CharField(max_length=255, default='', verbose_name='Тема сообщения')
    content = models.TextField(default='', verbose_name='Текст сообщения')
    mailing_start_time = models.DateTimeField(default=datetime.now, verbose_name='Время начала рассылки')
    mailing_stop_time = models.DateTimeField(default=datetime.now, verbose_name='Время окончания рассылки')
    period = models.CharField(default="daily", max_length=20, choices=PERIODS, verbose_name='Периодичность')
    status = models.CharField(default=STATUS_CREATED, max_length=20, choices=STATUSES, verbose_name='Статус')
    last_executed = models.DateTimeField(null=True, blank=True, verbose_name='Время последнего выполнения')

    def __str__(self):
        return f'Тема: {self.subject} С: {self.mailing_start_time} до:  {self.mailing_stop_time} периодичностью в: {self.period}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
