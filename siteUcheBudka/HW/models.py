from rest_framework import serializers
from .models import HW, Teacher, StudentHW, StudentClass, Profile, Student
from django.utils import timezone
from django.contrib.auth.models import User


class HWSerializers(serializers.Serializer):
    """Класс сериализатор для преобразования данных в JSON и обратно"""
    school_subject = serializers.CharField(max_length=50)
    task_text = serializers.CharField()
    fact_answer = serializers.CharField()
    student_class = serializers.PrimaryKeyRelatedField(queryset=StudentClass.objects.all())
    id = serializers.CharField(max_length=30)
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
    """Сериализатор для публикации домашки студентом. Можно дополнить функцией апдейт, что бы студент мог
    отредачить домашку"""
    school_subject = serializers.CharField(max_length=50, read_only=True)
    student_answer = serializers.CharField()
    hw = serializers.PrimaryKeyRelatedField(queryset=HW.objects.all())

    def create(self, validated_data):
        student = self.context['request'].user.student
        print("Текущий пользователь:", student)
        # Теперь создаем экземпляр StudentHW только с ожидаемыми полями
        return StudentHW.objects.create(student=student, complete=True, **validated_data)


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для реги юзеров..."""
    password = serializers.CharField(write_only=True)
    fullname = serializers.CharField(max_length=100, required=False)
    class_number = serializers.CharField(max_length=10, required=False, allow_blank=True, allow_null=True)
    subject_handling = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    is_teacher = serializers.BooleanField(required=False, default=False)
    is_student = serializers.BooleanField(required=False, default=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'fullname', 'class_number', 'subject_handling', 'is_teacher', 'is_student')

    def create(self, validated_data):
        is_teacher = validated_data.pop('is_teacher', False)
        is_student = validated_data.pop('is_student', False)
        fullname = validated_data.pop('fullname', '')
        class_number = validated_data.pop('class_number', None)
        subject_handling = validated_data.pop('subject_handling', None)

        user = User.objects.create_user(**validated_data)

        if is_student:
            Student.objects.create(user=user, fullname=fullname, class_number=class_number)
        else:
            Teacher.objects.create(user=user, fullname=fullname, subject_handling=subject_handling)
        Profile.objects.create(user=user, fullname=fullname, is_teacher=is_teacher, is_student=is_student)

        return User


class DiarySerializer(serializers.ModelSerializer):
    """Сериализатор для оценок"""
    school_subject = serializers.CharField(source='hw.school_subject')

    class Meta:
        model = StudentHW
        fields = ('school_subject', 'mark')
