from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активный')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        Group,
        verbose_name='Группы',
        blank=True,
        help_text='Группы, к которым принадлежит пользователь. Пользователь получает все разрешения,'
                  ' предоставленные каждой из его групп.',
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='Разрешения пользователя',
        blank=True,
        help_text='Конкретные разрешения для этого пользователя.',
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
    )
