from rest_framework import serializers
from .models import HW, Teacher, StudentHW, StudentClass
from django.utils import timezone


class HWSerializers(serializers.Serializer):
    """Класс сериализатор для преобразования данных в JSON и обратно"""
    school_subject = serializers.CharField(max_length=50)
    task_text = serializers.CharField()
    fact_answer = serializers.CharField()
    student_class = serializers.PrimaryKeyRelatedField(queryset=StudentClass.objects.all())
    # publish_time = serializers.DateTimeField()

    def create(self, validated_data):
        teacher = self.context['request'].user.teacher
        return HW.objects.create(teacher=teacher, **validated_data)

    def update(self, instance, validated_data):
        instance.school_subject = validated_data.get('school_subject')
        instance.task_text = validated_data.get('task_text')
        instance.fact_answer = validated_data.get('fact_answer')
        instance.publish_time = timezone.now()
        instance.save()
        return instance


class StudentHWSerializers(serializers.Serializer):
    school_subject = serializers.CharField(max_length=50, read_only=True)
    student_answer = serializers.CharField()
    hw = serializers.PrimaryKeyRelatedField(queryset=HW.objects.all())

    def create(self, validated_data):
        student = self.context['request'].user.student
        print("Текущий пользователь:", student)
        # Теперь создаем экземпляр StudentHW только с ожидаемыми полями
        return StudentHW.objects.create(student=student, complete=True, **validated_data)
