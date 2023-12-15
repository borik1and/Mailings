from django.core.management.base import BaseCommand
from django.utils import timezone
from mailing.models import Mailing
from clients.models import Clients
from django.core.mail import send_mail
from config import settings


class Command(BaseCommand):
    help = 'Send emails to clients for active mailings'

    def handle(self, *args, **options):
        now = timezone.now()
        mailings_to_send = Mailing.objects.filter(
            mailing_start_time__lte=now,
            mailing_stop_time__gte=now,
            status__in=['created', 'started']
        )

        for mailing in mailings_to_send:
            if mailing.last_executed and mailing.period == 'daily':
                # Проверка, выполнялась ли команда ранее и установлена ли она на ежедневное выполнение
                time_difference = now - mailing.last_executed
                if time_difference.days < 1:
                    # Если прошло менее 1 дня с последнего выполнения, пропустить эту рассылку
                    continue

            elif mailing.last_executed and mailing.period == 'weekly':
                # Проверка для еженедельного выполнения
                time_difference = now - mailing.last_executed
                if time_difference.days < 7:
                    # Если прошло менее 7 дней с последнего выполнения, пропустить эту рассылку
                    continue

            elif mailing.last_executed and mailing.period == 'monthly':
                # Проверка для ежемесячного выполнения
                time_difference = now - mailing.last_executed
                if time_difference.days < 30:
                    # Если прошло менее 30 дней с последнего выполнения, пропустить эту рассылку
                    continue

            clients_to_notify = Clients.objects.all()  # Подставьте здесь ваш запрос для выбора нужных клиентов
            user_emails = [client.email for client in clients_to_notify]

            send_mail(
                mailing.subject,
                mailing.content,
                settings.EMAIL_HOST_USER,
                user_emails,
                fail_silently=False,
            )

            mailing.last_executed = now
            mailing.save()

            self.stdout.write(self.style.SUCCESS(f'Emails sent for Mailing: {mailing.subject}'))