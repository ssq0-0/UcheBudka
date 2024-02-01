from rest_framework import permissions


class IsTeacherOnly(permissions.BasePermission):
    """Класс проверки прав для публикации домашней работы/удаления(в дальнейшем)/редактирования(в дальейшем)"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and hasattr(request.user, 'teacher'))

# class IsStudent(permissions.BasePermission):
#     def has_permission(self, request, view):