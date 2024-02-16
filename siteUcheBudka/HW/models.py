"""Модели студента, препода, домашней работы. Класс StudentHW хранит в себе домашнюю работу студента для
дальнейшей проверки с ответом преподавателя.

Класс HW - общий класс для хранения домашней работы, которую публикует преподаватель, ее может видеть любой,
в том числе и не авторизованный пользователь"""
from django.db import models
from django.contrib.auth.models import User


class StudentClass(models.Model):
    class_number = models.CharField(max_length=10, unique=True)
    students = models.ManyToManyField('Student', related_name='student_classes')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    class_number = models.CharField(max_length=5)

    def __str__(self):
        return self.fullname


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    subject_handling = models.CharField(max_length=60)

    def __str__(self):
        return self.fullname


class HW(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE, null=True)
    school_subject = models.CharField(max_length=50)
    task_text = models.TextField()
    fact_answer = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Предмет: {self.school_subject}, Учитель: {self.teacher}"

    def is_completed(self, student):
        return bool(StudentHW.objects.filter(hw=self, student=student, complete=True).exists())


class StudentHW(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    hw = models.ForeignKey(HW, on_delete=models.CASCADE)
    student_answer = models.TextField()
    complete = models.BooleanField(default=False)
    mark = models.IntegerField(null=True, blank=True)
