from django.contrib import admin

from users.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "preview_image")
    list_filter = ("id", "name")
    search_fields = ("id", "name")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "course", "preview_image", "video_url")
    list_filter = ("id", "course", "name")
    search_fields = ("id", "course__name", "name")
