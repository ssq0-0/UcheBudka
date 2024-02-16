from django.contrib import admin
from .models import HW, Teacher, Student, StudentHW, StudentClass


class StudentClassAdmin(admin.ModelAdmin):
    """Класс для более удобного администрирования модели"""
    list_display = ['class_number']
    filter_horizontal = ['students']


admin.site.register(HW)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentHW)
admin.site.register(StudentClass, StudentClassAdmin)
