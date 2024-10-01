
from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def check_activity():
    """Отключает пользователей, которые не входили в систему за последние 30 дней."""

    block_users = User.objects.filter(last_login__lt=timezone.now() - timedelta(days=30), is_active=True)
    block_users.update(is_active=False)
