"""Модели студента, препода, домашней работы. Класс StudentHW хранит в себе домашнюю работу студента для
дальнейшей проверки с ответом преподавателя.

Класс HW - общий класс для хранения домашней работы, которую публикует преподаватель, ее может видеть любой,
в том числе и не авторизованный пользователь"""
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_and_surname = models.CharField(max_length=50)
    class_number = models.CharField(max_length=5)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_and_surname = models.CharField(max_length=50)
    subject_handling = models.CharField(max_length=60)

    def __str__(self):
        return self.name_and_surname


class HW(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    school_subject = models.CharField(max_length=50)
    task_text = models.TextField()
    fact_answer = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)


class StudentHW(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    hw = models.ForeignKey(HW, on_delete=models.CASCADE)
    student_answer = models.TextField()
