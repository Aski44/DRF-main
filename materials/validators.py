from rest_framework.validators import ValidationError


url = "https://www.youtube.com"


def validate_url(value):
    if not value.startswith(url):
        raise ValidationError(
            f"В материалах урока могут содержаться видео только с {url}"
        )
