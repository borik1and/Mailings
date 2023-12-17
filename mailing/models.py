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
    last_executed = models.DateTimeField(**NULLABLE, verbose_name='Время последнего выполнения')
    attempt_status = models.BooleanField(**NULLABLE, verbose_name='Статус попытки')
    server_response = models.TextField(**NULLABLE, verbose_name='Ответ сервера')

    def __str__(self):
        return (f'Тема: {self.subject} С: {self.mailing_start_time} '
                f'до:  {self.mailing_stop_time} периодичностью в: {self.period} '
                f'Время последнего выполнения: {self.last_executed} Статус попытки: {self.attempt_status}')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class EmailLog(models.Model):
    subject = models.CharField(max_length=255)
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.subject} {self.sent_at} {self.status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
