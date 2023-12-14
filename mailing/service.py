from django.core.mail import send_mail, send_mass_mail


def send(user_mail):
    send_mail(
        'Test',
        'Test message',
        'borik1and@gmail.com',
        [user_mail],
        fail_silently=False,
    )


send('borik1and@gmail.com')