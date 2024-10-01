from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_url


class CourseSerializer(serializers.ModelSerializer):

    lessons_amount_in_course = serializers.SerializerMethodField()
    lessons = SerializerMethodField()

    def get_lessons_amount_in_course(self, obj):
        if obj.lesson_set.all().count():
            return obj.lesson_set.all().count()
        else:
            return 0

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.CharField(validators=[validate_url])

    class Meta:
        model = Lesson
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
