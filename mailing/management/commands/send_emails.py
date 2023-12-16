from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime
from mailing.models import Mailing
from clients.models import Clients
from django.core.mail import send_mail
from config import settings


class Command(BaseCommand):
    help = 'Send emails to clients for active mailings'

    def handle(self, *args, **options):
        now = datetime.now(timezone.utc)
        mailings_to_send = Mailing.objects.filter(
            mailing_start_time__lte=now,
            mailing_stop_time__gte=now,
            status__in=['created', 'started']
        )

        for mailing in mailings_to_send:
            try:
                if mailing.last_executed and self.should_skip_mailing(mailing, now):
                    continue

                clients_to_notify = Clients.objects.all()
                user_emails = [client.email for client in clients_to_notify]

                status = send_mail(
                    mailing.subject,
                    mailing.content,
                    settings.EMAIL_HOST_USER,
                    user_emails,
                    fail_silently=False,
                )

                mailing.last_executed = datetime.now()
                mailing.attempt_status = status

                # Сохраняем ответ сервера в поле server_response
                # mailing.server_response = 'Success'  # Или используйте фактический ответ сервера, если есть
                mailing.save()

                self.stdout.write(self.style.SUCCESS(f'Письмо с названием: {mailing.subject} отправлено.'))
            except Exception as e:
                # Обработка ошибок при отправке почты
                mailing.attempt_status = status
                mailing.save()

                # Сохраняем ответ сервера в поле server_response
                mailing.server_response = str(e)
                mailing.save()

                self.stdout.write(self.style.ERROR(f'Ошибка при отправке письма: {e}'))

    def should_skip_mailing(self, mailing, now):
        time_difference = now - mailing.last_executed

        if mailing.period == 'daily' and time_difference.days < 1:
            return True
        elif mailing.period == 'weekly' and time_difference.days < 7:
            return True
        elif mailing.period == 'monthly' and time_difference.days < 30:
            return True

        return False
