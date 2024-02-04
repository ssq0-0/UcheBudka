from django.shortcuts import render
from rest_framework.views import APIView
from .models import HW, StudentHW
from .serializers import HWSerializers, StudentHWSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from HW.permissions import IsTeacherOnly, IsStudentOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

# переделать методы пост, пут/патч, дестрой училки, заменить классом RetrieveDestroyAPIView


class HWAPIGetView(ListAPIView):
    """Обычный класс для GET запроса на список домашних заданий"""
    queryset = HW.objects.all()
    serializer_class = HWSerializers
    permission_classes = (IsAuthenticated, )


class HWAPIPostView(CreateAPIView):
    """Класс для публикации домашки учителем"""
    queryset = HW.objects.all()
    serializer_class = HWSerializers
    permission_classes = (IsTeacherOnly, )


class HWAPIUpdateView(UpdateAPIView):
    """Класс для апдейта дз преподом"""
    queryset = HW.objects.all()
    serializer_class = HWSerializers
    permission_classes = (IsTeacherOnly, )


class HWAPIDestroyView(DestroyAPIView):
    """Класс удаления записи преподом"""
    queryset = HW.objects.all()
    serializer_class = HWSerializers
    permission_classes = (IsTeacherOnly, )


class StudentAPIView(APIView):
    permission_classes = [IsStudentOnly]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            item = get_object_or_404(HW, pk=pk)
            serializer = HWSerializers(item)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = StudentHWSerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
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


def test_(request):
    return render(request, 'HW/test.html')
