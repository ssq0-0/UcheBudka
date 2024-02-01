from django.shortcuts import render
from rest_framework.views import APIView
from .models import HW
from .serializers import HWSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


class HWAPIView(APIView):
    """Общий Класс представления домашней работы"""
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            items = HW.objects.all()
            serializer = HWSerializers(items, many=True)
        else:
            item = get_object_or_404(HW, pk=pk)
            serializer = HWSerializers(item)

        return Response(serializer.data)

    def post(self, request):
        """Реализация публикации домашней работы в зависимости от того кто это пытается сделать
        ученик или учитель"""
        serializer = HWSerializers(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        # реализовать в дальнейшем изменения домашки в целом от учителя или изменение ТОЛЬКО ответа
        # от ученика
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
