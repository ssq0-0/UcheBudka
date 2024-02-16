from django.shortcuts import render
from rest_framework.views import APIView
from .models import HW, StudentHW, Teacher, StudentClass, Student
from .serializers import HWSerializers, StudentHWSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status, generics, viewsets
from HW.permissions import IsTeacherOnly, IsStudentOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

# переделать методы пост, пут/патч, дестрой училки, заменить классом RetrieveDestroyAPIView


class HWAPIModelViewSet(viewsets.ModelViewSet):
    """Дефолт гет запрос"""
    queryset = HW.objects.all()
    serializer_class = HWSerializers
    permission_classes = (IsAuthenticated, )


class TeacherMethodsAPIViewSet(viewsets.ModelViewSet):
    """Вьюсет для препода, CRUD операции с домашней работой"""
    queryset = HW.objects.all()
    serializer_class = HWSerializers
    permission_classes = (IsTeacherOnly, )


class TeacherMarkAPIViewSet(APIView):
    permission_classes = [IsTeacherOnly,]

    def post(self, request, *args, **kwargs):
        student_hw_id = request.data.get('student_hw_id')  # Используйте уникальный ID записи работы студента
        new_mark = request.data.get('mark')

        try:
            # Получаем запись работы студента по её уникальному ID
            student_hw = StudentHW.objects.get(id=student_hw_id)
            student_hw.mark = new_mark
            student_hw.save()
            return Response({"message": "Mark is set"})
        except StudentHW.DoesNotExist:
            return Response({"error": "Student HW assignment not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class HWParamsFroStudentAPIView(APIView):
    """Эндпоинт для студентов. Эндпоинт для главное страницы, а так же для будующей фильтрации
    по параметрам. Возвращает только те домашние задания, которые НЕ ВЫПОЛНЕНЫ"""
    permission_classes = [IsStudentOnly, ]

    def get(self, request, *args, **kwargs):
        student = request.user.student
        student_class = student.class_number
        student_class_obj = StudentClass.objects.filter(class_number=student_class).first()

        if not student_class_obj:
            return Response({"error": "Student class not found."}, status=400)

        items = HW.objects.filter(student_class=student_class_obj)
        not_complete = [hw for hw in items if not hw.is_completed(student)]
        serializer = HWSerializers(not_complete, many=True)
        return Response(serializer.data)


class StudentAPIView(APIView):
    """Гет и пост запросы для студента. Есть проверка на публикацю домашки. Если студент уже ранее
    опубликовал дз - в след раз не получится, ибо ответ уже дан"""
    permission_classes = [IsStudentOnly]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            item = get_object_or_404(HW, pk=pk)
            student = request.user.student
            serializer = HWSerializers(item)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        hw_item = HW.objects.get(pk=pk)
        student = request.user.student
        if StudentHW.objects.filter(hw=hw_item, student=student, complete=True).exists():
            return Response({"message": "You have already completed this homework."}, status=status.HTTP_200_OK)

        serializer = StudentHWSerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            student_hw_instance = serializer.save()
            student_hw_instance.complete = True
            student_hw_instance.save()
        else:
            return Response({'error': 'ERROR'})

        # из пришедшего реквеста вытаскивает pk и делаем гет запрос на общую модель домашки
        hw_item = HW.objects.get(pk=serializer.validated_data['hw'].pk)

        if hw_item.fact_answer.strip().lower() == serializer.validated_data['student_answer'].strip().lower():
            return Response({"post": "It's true!"})
        else:
            return Response({"post": "It's false("})




def login_(request):
    return render(request, 'HW/hw.html')


def main_(request):
    return render(request, 'HW/main.html')
