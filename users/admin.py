from django.contrib import admin

from users.models import Payments, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email")
    list_filter = ("id", "email")
    search_fields = ("id", "email")


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "payment_date",
        "course",
        "lesson",
        "amount",
        "payment_type",
    )
    list_filter = ("id", "user", "course", "lesson", "payment_type")
    search_fields = ("id", "user__email", "course__name", "lesson__name")
