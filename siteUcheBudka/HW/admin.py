from django.contrib import admin
from .models import HW, Teacher, Student, StudentHW


admin.site.register(HW)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentHW)
