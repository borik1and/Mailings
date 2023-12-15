from django.core.mail import send_mail
from config import settings


# def send(user_mails):
#     send_mail(
#         'Test Subject',
#         'Test новое письмо',
#         settings.EMAIL_HOST_USER,
#         user_mails,  # Передаем список адресов как аргумент
#         fail_silently=False,
#     )
