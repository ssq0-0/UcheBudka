from rest_framework.views import APIView
from .models import HW, StudentHW
from .serializers import HWSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from HW.permissions import IsTeacherOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class HWAPIView(APIView):
    """Общий Класс представления домашней работы как полным списком, так и по отдельному заданию"""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        # просматривать домашнюю работу может кто угодно, даже не залогинившись
        pk = kwargs.get('pk')
        if not pk:
            items = HW.objects.all()
            serializer = HWSerializers(items, many=True)
        else:
            item = get_object_or_404(HW, pk=pk)
            serializer = HWSerializers(item)

        return Response(serializer.data)

    def post(self, request):
        # Реализация публикации домашней работы в зависимости от того кто это пытается сделать
        # учитель или кто либо другой
        permissions = IsTeacherOnly()
        if permissions.has_permission(request, self):
            serializer = HWSerializers(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'post': serializer.data})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Публиковать задания может только учитель'})

    def put(self, request, *args, **kwargs):
        # реализовать изменения только со стороны преподавателя
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Not find this item in DB'})
        try:
            instance = HW.objects.get(pk=pk)
        except:
            return Response({'error': 'Not find this item in DB'})
        serializer = HWSerializers(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        # предоставить возможность удаления только преподавателю
        hw = get_object_or_404(HW, pk=kwargs.get('pk'))
        hw.delete()
        return Response(({'message': 'Deleted successfully'}, status==status.HTTP_204_NO_CONTENT))


class StudentHWAPIView(APIView):
    """Класс представления для домашней работы. Этот класс будет принимать домашнюю работу и в дальнейшем
    сравнивать ответы, которые дал препод с ответами учеников и возвращать treu/false. В процессе
    разработки будет реализована возможность предоставления домашки в различном виде, в том числе и фото"""
    pass

