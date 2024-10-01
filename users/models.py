from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import datetime
from django.utils.timezone import now

from materials.models import Course, Lesson

payment_choices = (
    ("Наличные", "Наличные"),
    ("Перевод на счет", "Перевод на счет"),
)


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="электронная почта", help_text="укажите эл. почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="телефон",
        blank=True,
        null=True,
        help_text="укажите телефон",
    )
    city = models.CharField(
        max_length=35,
        verbose_name="город",
        blank=True,
        null=True,
        help_text="укажите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="аватар",
        help_text="загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.email


class Payments(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="пользователь",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    payment_date = models.DateTimeField(
        default=now, verbose_name="Дата оплаты", blank=True, null=True
    )
    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    lesson = models.ForeignKey(
        Lesson,
        verbose_name="Урок",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    amount = models.PositiveIntegerField(verbose_name="Стоимость курса", help_text="Укажите стоимость курса"
    )
    payment_type = models.CharField(
        max_length=50,
        verbose_name="Способ оплаты",
        default="Перевод на счет",
        choices=payment_choices,
    )
    session_id = models.CharField(
        max_length=250,
        verbose_name="ID сессии",
        blank=True,
        null=True,
        help_text="Укажите ID сессии",
    )
    payment_link = models.URLField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату",
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return self.amount
