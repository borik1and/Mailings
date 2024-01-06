from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='manager@mailing.com',
            first_name='Admin',
            last_name='prod',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )

        user.set_password('1975')
        user.save()

        self.stdout.write(self.style.SUCCESS('Менеджер успешно создан.'))
